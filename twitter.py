import tweepy
import time

auth = tweepy.OAuthHandler('api key','api secret key')

auth.set_access_token('access token', 'access token secret')

api = tweepy.API(auth, wait_on_rate_limit= True, wait_on_rate_limit_notify= True)

user = api.me()

search = 'javascript'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet liked')
        tweet.favorite()
        time.sleep(6)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
