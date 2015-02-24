#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import random


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    pg = connect()
    c = pg.cursor()
    c.execute("DELETE FROM matches")
    pg.commit()
    pg.close()


def deletePlayers():
    """Remove all the player records from the database."""
    pg = connect()
    c = pg.cursor()
    c.execute("DELETE FROM players")
    pg.commit()
    pg.close()


def countPlayers():
    """Returns the number of players currently registered."""
    pg = connect()
    c = pg.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    num_players = c.fetchall()[0][0]
    pg.close
    return num_players


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  
  
    Args:
      name: the player's full name (need not be unique).
    """
    pg = connect()
    c = pg.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    pg.commit()
    pg.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    pg = connect()
    c = pg.cursor()
    c.execute("SELECT * FROM tournament_classification")
    classification = c.fetchall() 
    pg.close()
    return classification


def reportMatch(player1, player2, winner):
    """Records the outcome of a single match between two players.

    Args:
      player1, player2:  the id number of the players
      winner: player1's id (player1 wins), player2's id (player2 wins) 
              or None (tied game)
    """
    pg = connect()
    c = pg.cursor()
    c.execute("INSERT INTO matches (player1, player2, winner) VALUES (%s, %s, %s)", 
              (player1, player2, winner))
    pg.commit()
    pg.close()
 

def evenPairings(standings):
    """Auxiliar method to pair even players.

    Args:
    standings: the list of players and win records

    Returns:
    A list of tuples, each of which contains (id1, name1, id2, name2)
    """
    pairList = []
    count = 0
    while count < len(standings) - 1:
        p1 = standings[count]
        p2 = standings[count + 1]
        pairList.append((p1[0], p1[1], p2[0], p2[1]))
        count += 2
    return pairList


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Each player appears exactly once in the pairings. If there is an odd 
    number of players, randomly assign one player a 'bye' (skipped round). 
    A bye counts as a free win. A player should not receive more than one 
    bye in a tournament.
    Each player is paired with another player with an equal or nearly-equal 
    win record, that is, a player adjacent to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id (or "bye")
        name2: the second player's name (or "skipped round")
    """
    pg = connect()
    c = pg.cursor()

    pairList = []
    classification = playerStandings()
    
    #take into account odd number of players by assigning a 'bye' round to one 
    if len(classification)%2 != 0:
        
        #make sure that not all players already had an skipped round
        c.execute("SELECT skipped_round FROM players")
        rows = c.fetchall()
        skips = [row[0] for row in rows]
        
        if skips.count(True) != len(skips): 

            #there's at least 1 player without a 'bye' round
            r = range(0, len(classification))
            found = False

            while not found:
            #Randomly pick one player from the classification list
            #If she/he doesn't have a 'bye' round:
                #Add the free win
                #Add the player to the final swiss pairing list
                #Remove the player from the remaining list of players to be paired
                
                rand_index = random.choice(r)
                player = classification[rand_index]
                c.execute("SELECT skipped_round FROM players WHERE players.id = (%s)",
                        (player[0],))
                already_skipped = c.fetchall()[0][0]
                
                if not already_skipped: #player didn't skipped a round yet
                    c.execute("UPDATE players SET skipped_round = TRUE WHERE players.id = (%s)",
                    (player[0],))
                    pg.commit()
                    pg.close()
                    found = True
                    #add a free win match to the player
                    reportMatch(player[0], None, player[0])
                    #add player to result list
                    pairList.append((player[0], player[1], "bye", "skipped round"))
                    #remove player from classification list
                    del classification[rand_index]
            
            #match the rest of even players
            pairList.extend(evenPairings(classification))
    
    #even number of players
    else:
        pairList.extend(evenPairings(classification))
    
    return pairList
