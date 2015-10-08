import time
import praw
import praw.helpers
from pprint import pprint

USER_AGENT_STR = 'PRAW stream testing by /u/moosekin v 1.0.'
SUBREDDITS = "nfl+fantasyfootball"

if __name__ == '__main__':

	r = praw.Reddit(USER_AGENT_STR)
	
	#stream of new posts sample
	new_posts = praw.helpers.submission_stream(r, SUBREDDITS, limit=10)
	for post in new_posts:
		print post.title

#stream of comments
#	new_comments = praw.helpers.comment_stream(r, SUBREDDITS, limit = 100)

#	for c in new_comments:
#		print c.link_title
#		print c.body