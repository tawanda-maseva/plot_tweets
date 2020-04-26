from tw_visualizations import Timeline, Tweets_by, Hashtag
import data_processing as dp


tawanda_credentials = '/Users/user/Desktop/python_work/CHAPTER_02/04_working_with_APIs/twitter_project/twitter_credentials.json'
#timmy = Timeline('timmy', tawanda_credentials)
#elonmusk = Tweets_by('elonmusk', tawanda_credentials)
# trump = Tweets_by('realDonaldTrump', tawanda_credentials)

#got = Hashtag('#ForTheThrone', tawanda_credentials)

def main():
	'''View tweets by likes or retweets'''
	dp.welcome_msg()
	user_input = dp.verify_user_input()

	while user_input != 'q':
		if user_input == '1':
			show = True
			while show:
				#Plot tweets from timeline
				timeline_tweets = Timeline('timmy', tawanda_credentials)
				timeline_tweets.tweetsby('likes')
				timeline_tweets.tweetsby('retweets')
				print('Done! See plots in output folder :)\n')

				next_click = input('Refresh plots or quit? (r/q): ')
				if next_click == 'q':
					show = False  # exit
				elif next_click == 'r':
					timmy.refresh_tweets()
				else:
					print('Invalid input')

		elif user_input == '2':
			show = True
			while show:
				# Plot tweets by a given user
				account_name = input('Please enter the @username: ')
				account_tweets = Tweets_by(account_name, tawanda_credentials)
				account_tweets.tweetsby('likes')
				account_tweets.tweetsby('retweets')
				print('Done! See plots in output folder :)\n')

				next_click = input('Refresh plots or quit? (r/q): ')
				if next_click == 'q':
					show = False  # exit
				elif next_click == 'r':
					account_tweets.refresh_tweets()

		elif user_input == '3':
			show = True
			while show:
				# Plot tweets by a given hashtag
				hashtag = input('Please enter the hashtag: ')
				hashtag_tweets = Hashtag(hashtag, tawanda_credentials)
				hashtag_tweets.tweetsby('likes')
				hashtag_tweets.tweetsby('retweets')
				print('Done! See plots in output folder :)\n')

				next_click = input('Refresh plots or quit? (r/q): ')
				if next_click == 'q':
					show = False  # exit
				elif next_click == 'r':
					hashtag_tweets.refresh_tweets()

		dp.welcome_msg()
		user_input = dp.verify_user_input()












		#got.tweetsby('likes')
		#got.tweetsby('retweets')

		#elonmusk.account_tweetsby('likes', 'red')
		#elonmusk.account_tweetsby('retweets', 'yellow')

		#trump.account_tweetsby('likes')
		#trump.account_tweetsby('retweets')

		#next_click = input('Refresh or quit? (r/q): ')
		#if next_click == 'q':
		#	show = False  # exit
		#elif next_click == 'r':
		#	timmy.refresh_tweets()
			#elonmusk.refresh_tweets()
			#trump.refresh_tweets()
			#got.refresh_tweets()
		#else:
		#	print('Invalid input')

main()


