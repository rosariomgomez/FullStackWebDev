import urllib

PROFANITY_CHECK_WEB = "http://www.wdyl.com/profanity?q="

def read_text():
	quotes = open('movie_quotes.txt')
	contents = quotes.read()
	check_profanity(contents)
	quotes.close()

def check_profanity(text_to_check):
	connection = urllib.urlopen(PROFANITY_CHECK_WEB + text_to_check)
	output = connection.read()
	connection.close()

	if 'true' in output:
		print('Alert! Check your text')
	elif 'false' in output:
		print('No profanity found')
	else:
		print('Sorry, there was a problem scanning your text')
	
read_text()