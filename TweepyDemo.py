__author__ = 'hxcxor'

import tweepy
import json

# consumer keys and token, for oauth
consumer_key=
consumer_secret=
access_token=
access_token_secret=

# to search using cursor
status = tweepy.Cursor(api.search, q='tarasenko')

""" class MyListener(tweepy.StreamListener):
    def on_data(self, data):

        decoded = json.loads(data)

        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    l = MyListener()
    # construct api instance
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = tweepy.Stream(auth, l)

    print "Showing all new tweets for 'Tarasenko':"
    stream.filter(track=['Tarasenko']) """

# to use Json raw data