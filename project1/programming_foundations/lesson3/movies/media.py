import webbrowser

class Video(object):
	"""This class provides a way to store video related information"""

	def __init__(self, title, storyline, poster_image_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url

class Movie(Video):
	"""This class provides a way to store movie related information"""

	def __init__(self, movie_title, movie_storyline, movie_duration,
				poster_image, trailer_youtube):
		Video.__init__(self, movie_title, movie_storyline, 
					   poster_image)
		self.trailer_youtube_url = trailer_youtube
		self.duration = movie_duration

	def show_trailer(self):
		'''Open a pop-up window with the movie trailer'''
		webbrowser.open(self.trailer_youtube_url)

class Episode():
	"""This class provides a way to store information about tvshows' 
	episodes"""
	def __init__(self, episode_title, episode_storyline, 
				episode_duration, episode_season, episode_number):
		self.title = episode_title
		self.storyline = episode_storyline
		self.duration = episode_duration 
		self.season = episode_season
		self.number = episode_number

class TvShow(Video):
	"""This class provides a way to store TvShow related information"""

	def __init__(self, tvshow_title, tvshow_storyline, 
				poster_image, tv_station, episodes):
		Video.__init__(self, tvshow_title, tvshow_storyline, 
					   poster_image)
		self.tv_station = tv_station
		self.episodes = episodes

