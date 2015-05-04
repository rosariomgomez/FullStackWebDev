import webbrowser

class Video(object):
	"""Stores video related information"""

	def __init__(self, title, storyline, poster_image_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url


class Movie(Video):
	"""Stores movie related information. Inherits from Video"""

	def __init__(self, movie_title, movie_storyline, movie_duration,
							poster_image, trailer_youtube):
		Video.__init__(self, movie_title, movie_storyline, poster_image)
		self.trailer_youtube_url = trailer_youtube
		self.duration = movie_duration

	def show_trailer(self):
		"""Open a pop-up window with the movie trailer"""
		webbrowser.open(self.trailer_youtube_url)


class Episode(object):
	"""Stores information about the episodes of a tvshow object"""

	def __init__(self, episode_title, episode_storyline, episode_duration,
							episode_season, episode_number):
		self.title = episode_title
		self.storyline = episode_storyline
		self.duration = episode_duration
		self.season = episode_season
		self.number = episode_number


class TvShow(Video):
	"""Stores TvShow related information. Inherits from Video.
	Episodes is a list of episode objects"""

	def __init__(self, tvshow_title, tvshow_storyline, poster_image,
							tv_station, episodes):
		Video.__init__(self, tvshow_title, tvshow_storyline, poster_image)
		self.tv_station = tv_station
		self.episodes = episodes

