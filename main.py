from tw_visualizations import Timeline, Tweets_by, Hashtag


tawanda_credentials = '/Users/user/Desktop/python_work/CHAPTER_02/04_working_with_APIs/twitter_project/twitter_credentials.json'
timmy = Timeline('timmy', tawanda_credentials)
#elonmusk = Tweets_by('elonmusk', tawanda_credentials)
# trump = Tweets_by('realDonaldTrump', tawanda_credentials)

got = Hashtag('#ForTheThrone', tawanda_credentials)

def main():
	'''View tweets by likes or retweets'''
	show = True
	while show:

		timmy.tweetsby('likes')
		timmy.tweetsby('retweets')

		#got.tweetsby('likes')
		#got.tweetsby('retweets')

		#elonmusk.account_tweetsby('likes', 'red')
		#elonmusk.account_tweetsby('retweets', 'yellow')

		#trump.account_tweetsby('likes')
		#trump.account_tweetsby('retweets')

		next_click = input('Refresh or quit? (r/q): ')
		if next_click == 'q':
			show = False  # exit
		elif next_click == 'r':
			timmy.refresh_tweets()
			#elonmusk.refresh_tweets()
			#trump.refresh_tweets()
			#got.refresh_tweets()
		else:
			print('Invalid input')

main()


