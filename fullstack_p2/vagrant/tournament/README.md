## Project 2: Swiss-system tournament implementation

### How to run the code
After following the detailed instructions in the <a href="https://www.udacity.com/wiki/ud197/install-vagrant">course documentation,</a> run the following commands into the VM:
```
cd /vagrant/tournament
python tournament_test.py
```
  
This will run the battery of tests against the code. All tests should pass with the following output in the terminal window:

```
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
9. Odd number of players correctly paired. Skipped player has a free win
10. Skipped matches are correctly given in a tournament with an odd number of players
11. Players are correclty matched with tied games
Success!  All tests pass!

```

### Code versions

* <a href="https://github.com/rosariomgomez/fullstack-nanodegree-vm/tree/1aae4fff6ef2d183e9af5bf0fc99e4e2c8d26d08/vagrant/tournament">v1.0:</a> Basic implementation
* <a href="https://github.com/rosariomgomez/fullstack-nanodegree-vm/tree/4f87b127a5fbcca02cfeb53876a6f16399746814/vagrant/tournament">v2.0:</a> Allow an odd number of players
* <a href="https://github.com/rosariomgomez/fullstack-nanodegree-vm/tree/b68e5174c936f2cb825004df9dbcc7c5d90f100e/vagrant/tournament">v3.0:</a> Support games where a draw (tied game) is possible