import time
import webbrowser

num_breaks = 1
total_breaks = 3

print("This program started on "+ time.ctime())
while num_breaks <= total_breaks:
	time.sleep(10)
	webbrowser.open('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
	num_breaks = num_breaks + 1
