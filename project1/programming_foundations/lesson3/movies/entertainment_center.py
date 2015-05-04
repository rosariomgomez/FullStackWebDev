'''
This file contains the manual creation of a list of movie and Tv shows and
episodes objects. These objects are passed as arguments to the open_page()
method call from the fresh_tomatoes.py file
'''

import fresh_tomatoes
from media import Movie, Episode, TvShow

#Movie creation
toy_story = Movie('Toy Story',
					'A wonderful story of toys', 81,
					'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
					'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = Movie('Avatar',
				'A marine on an alien planet', 178,
				'http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
				'https://www.youtube.com/watch?v=5PSNL1qE6VY')

school_of_rock = Movie('School of Rock',
					'Using rock music to learn', 109,
					'http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
					'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = Movie('Ratatouille',
					'A rat that is a chef in Paris', 115,
					'http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
					'https://www.youtube.com/watch?=v=c3sBBRxDAqk')

midnight_in_paris = Movie('Midnight in Paris',
					'Going back in time to meet authors', 100,
					'http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
					'https://www.youtube.com/watch?v=BYRWfS2s2v4')

hunger_games = Movie('Hunger Games',
					 'A real reality show', 123,
					 'http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
					 'https://www.youtube.com/watch?v=PbA63a7H0bo')

#List of movies
movies = [toy_story, avatar, school_of_rock, ratatouille,
					midnight_in_paris, hunger_games]


#Episodes creation (Title, Storyline, duration, season, episode)
breaking_bad_e1_s1 = Episode('Pilot',
							"Walter White, a 50-year old chemistry teacher, secretly begins \
							making crystallized methamphetamine to support his family after \
							learning that he has terminal lung cancer. He teams up with a former \
							student, Jesse Pinkman, who is a meth dealer. Jesse tries to sell the \
							meth they made, but the dealers snatch him and make him show them their \
							lab, which is in an old RV. Walt knows the dealers intend to kill him, \
							so he poisons them while pretending to share his recipe.",
							58, 1, 1)

breaking_bad_e2_s1 = Episode('Cats in the Bag',
							"Walt and Jesse try to dispose of the two bodies in the RV, which \
							becomes increasingly complicated when one of them, Krazy-8, wakes up. \
							They eventually imprison him in Jesse's basement. Meanwhile, Skyler \
							grows suspicious of Walter's recent behavior and discovers that their \
							baby is a girl. Jesse disposes of the body of the other dealer, Emilio Koyama, \
							using hydrofluoric acid as per Walt's instructions, but ignores Walt's warning \
							to use a plastic bin and instead destroys his bathtub in the process.",
							48, 1, 2)

#TVShow creation (Title, Storyline, poster, trailer, station, episodes list)
breaking_bad = TvShow('Breaking bad', 'The secret lifestyle of a chemistry teacher',
					  'http://upload.wikimedia.org/wikipedia/commons/4/48/Breaking_Bad_logo.png',
					  'AMC',
					  [breaking_bad_e1_s1, breaking_bad_e2_s1])


modern_family = TvShow('Modern Family', 'A comedy that follows the lives of a peculiar family',
						'http://upload.wikimedia.org/wikipedia/en/5/53/Modern_Family_Promo_Season_1.jpg',
						'ABC', [])

#List of tv shows
tvshows = [breaking_bad, modern_family]

fresh_tomatoes.open_page(movies, tvshows)
