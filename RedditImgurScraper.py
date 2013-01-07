"""
Reddit photo scraper
Downloads the imgur photos from the top N photos from the specified subreddit.
Nate Brennand
"""

from string import replace
import praw
import pyimgur
from sys import argv

imgurFilter = [".jpg",".gif","http://imgur.com/","http://i.imgur.com/"]

if len(argv) != 4:
	print "Usage: python %s <subreddit> <# of photos> <time period>" %argv[0]
	exit(1)

scrape = praw.Reddit(user_agent="imgur photo scraper by u/Twigger")
submissions = scrape.get_subreddit(str(argv[1])).get_top(limit = int(argv[2]),url_data={'t':str(argv[3])})

print "imgur hashes:"
hashes = []
for y in submissions:
	x = str(y.url)
	if "imgur" in x and "a/" not in x:
		for i in imgurFilter:
			x = replace(x,i,"")
		print x
		hashes.append(x)

for x in hashes:
	pyimgur.download_image( x, "large_thumbnail" )
	print "Downloaded %s" %x
