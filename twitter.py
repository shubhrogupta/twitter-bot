import tweepy
import time

auth = tweepy.OAuthHandler('B2hri15fL3UKlq5Kty8fObqy0','Xztav1G3nXqhXSHuuQ3UEXRi2BIgglskDRuL2kJFaF97KHSOMI')

auth.set_access_token('819554966998282240-WXfd4GqpDh1uUBlV13SK3xt6ZY2mnaY', 'MWBrwVFfISXKcHwoAwtLpiCCVbhqVWPztm7Za5Wt65Nwh')

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
