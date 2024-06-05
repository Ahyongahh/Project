import tweepy 
client = tweepy.Client(bearer_token= 'AAAAAAAAAAAAAAAAAAAAAAGCuAEAAAAA%2FSySKvjPjF%2FibpaN1xT3gfR%2B6Lc%3DQ6f98OQ8asS1leKtjeYGQsqStsVo7tQEabd0i7vWElSkjrrpXi')

id = '@Ahyong___'

tweets = client.get_users_tweets(id=id, tweet_field= ['context_annotation' , 'created_at', 'geo'])

for tweet in tweets.data:
    print(tweet)