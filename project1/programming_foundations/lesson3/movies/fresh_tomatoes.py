import webbrowser
import os
import re
import datetime

# Styles and scripting for the page
main_page_head = '''
<head>
	<meta charset="utf-8">
	<title>Fresh Tomatoes!</title>

	<!-- Bootstrap 3 -->
	<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
	<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
	<script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
	<style type="text/css" media="screen">
		body {
			padding-top: 80px;
		}
		#trailer .modal-dialog {
			margin-top: 200px;
			width: 640px;
			height: 480px;
		}
		.hanging-close {
			position: absolute;
			top: -12px;
			right: -12px;
			z-index: 9001;
		}
		#trailer-video {
			width: 100%;
			height: 100%;
		}
		.movie-tile {
			margin-bottom: 20px;
			padding-top: 20px;
		}
		.movie-tile:hover {
			background-color: #EEE;
			cursor: pointer;
		}
		.scale-media {
			padding-bottom: 56.25%;
			position: relative;
		}
		.scale-media iframe {
			border: none;
			height: 100%;
			position: absolute;
			width: 100%;
			left: 0;
			top: 0;
			background-color: white;
		}
	</style>
	<script type="text/javascript" charset="utf-8">
		// Pause the video when the modal is closed
		$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
			// Remove the src so the player itself gets removed, as this is the only
			// reliable way to ensure the video stops playing in IE
			$("#trailer-video-container").empty();
		});
		// Start playing the video whenever the trailer modal is opened
		$(document).on('click', '.movie-tile', function (event) {
			var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
			var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
			$("#trailer-video-container").empty().append($("<iframe></iframe>", {
			  'id': 'trailer-video',
			  'type': 'text-html',
			  'src': sourceUrl,
			  'frameborder': 0
			}));
		});
		// Animate in the movies when the page loads
		$(document).ready(function () {
		  $('.movie-tile').hide().first().show("fast", function showNext() {
			$(this).next("div").show("fast", showNext);
		  });
		});
	</script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
	<!-- Trailer Video Modal -->
	<div class="modal" id="trailer">
	  <div class="modal-dialog">
		<div class="modal-content">
		  <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
			<img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
		  </a>
		  <div class="scale-media" id="trailer-video-container">
		  </div>
		</div>
	  </div>
	</div>
	
	<!-- Main Page Content -->
	<!-- Top navigation bar -->
	<div class="container">
	  <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
		<div class="container">
		  <div class="navbar-header">
			<a class="navbar-brand" href="#">Fresh Tomatoes Trailers</a>
		  </div>
		  <div class="navbar-collapse collapse">
			<ul class="nav navbar-nav">
			   <li><a href="#movies">Movies</a></li>
			   <li><a href="#tvshows">TV Shows</a><li>
			</ul>
		  </div>
		</div>
	  </div>
	</div>
	<!-- Movies and TvShows section --> 
	<div class="container">
	  <div id='movies'>
		<h2>Movies</h2>
		{movie_tiles}
	  </div>
	  <hr>
	  <div id='tvshows'>
		<h2>TV Shows</h2>
		{tvshow_tiles}
	  </div>
	</div>
  </body>
</html>
'''

# A single movie entry html template, open trailer in trailer video modal
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
	<img src="{poster_image_url}" width="220" height="342">
	<h2>{movie_title}</h2>
	<p>{movie_storyline}<br>
	<i>Duration: {movie_duration} h.</i></p>
</div>
'''

# A single tvshow entry html template, div closed after including episode information
tvshow_tile_content = '''
<div class="col-md-6 col-lg-4 tvshow-tile text-center">
	<img src="{poster_image_url}" width="200" height="300">
	<h2>{tvshow_title}</h2>
	<p>{tvshow_storyline}<br>
	<i>Station: {tvshow_station}</i>
	</p>
'''

# A single episode entry html template
episode_tile_content = '''
<div class="text-left">
	<a href='#' class="episode-tile" data-toggle="modal" data-target="#{episode_id}">
	{episode_title}</a>
	<p>Season: {episode_season}, Episode: {episode_number}<br>
	<i>Duration: {episode_duration}</i>
	</p>
</div>

<!-- Episode Modal. Code based on the static example here: http://getbootstrap.com/javascript/ -->
<div class="modal fade" id="{episode_id}">
  <div class="modal-dialog">
	<div class="modal-content"> 
	  <div class="modal-header">
		<a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
		  <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
		</a>
		<h4 class="modal-title">{episode_title} storyline</h4>
	  </div>
	  <div class="modal-body" id="episode-container">
		<p class="text-left">{episode_storyline}</p>
	  </div>
	</div>
  </div>
</div>
'''


def extract_youtube_info(url):
  '''Extract the youtube ID from the url'''
  youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
  youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', url)
  return youtube_id_match.group(0) if youtube_id_match else None

def create_movie_tiles_content(movies):
	'''Generate the HTML content for the movie section of the html page
	   Input: list of movies
	   Output: HTML code
	'''
	content = ''
	for movie in movies:
		trailer_youtube_id = extract_youtube_info(movie.trailer_youtube_url)

		# Append the tile for the movie with its content filled in
		content += movie_tile_content.format(
			movie_title=movie.title,
			movie_storyline=movie.storyline,
			movie_duration=str(datetime.timedelta(minutes=movie.duration)),
			poster_image_url=movie.poster_image_url,
			trailer_youtube_id=trailer_youtube_id
		)
	return content

def create_episode_tiles_content(episodes):
	'''Generate the HTML content for the episodes section that resides inside 
	   the tvshow_tiles of the html page
	   Input: list of episodes
	   Output: HTML code
	'''
	content = '<h4 align="left">Episodes:</h4>'
	
	if episodes:
	  for episode in episodes:

		# Append the episodes information
		  content += episode_tile_content.format(
			  episode_id=episode.title.replace(' ', ''),
			  episode_title=episode.title,
			  episode_storyline=episode.storyline,
			  episode_season=episode.season,
			  episode_number=episode.number,
			  episode_duration=episode.duration
		  )
	else:
	  content += 'No episodes added yet'
	return content

def create_tvshow_tiles_content(tvshows):
	'''Generate the HTML content for the tvshows section of the html page
	   Input: list of tvshows
	   Output: HTML code
	'''
	content = ''
	for tvshow in tvshows:

		# Append the tile for the tvshow with its content filled in
		content += tvshow_tile_content.format(
			tvshow_title=tvshow.title,
			tvshow_storyline=tvshow.storyline,
			poster_image_url=tvshow.poster_image_url,
			tvshow_station=tvshow.tv_station,
			tvshow_episodes=tvshow.episodes)

		# Append to each tvshow its episodes html and close the tvshow div section
		content += create_episode_tiles_content(tvshow.episodes) + '</div>'
	return content

def open_page(movies, tvshows):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(
								movie_tiles=create_movie_tiles_content(movies),
								tvshow_tiles=create_tvshow_tiles_content(tvshows))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
  