from __future__ import absolute_import, print_function

# Import modules
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import re as regex


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        print(status.text)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == '__main__':
    # Variables that contains the user credentials to access Twitter API 
    access_token = '63437096-AayyBAcqCt5Ruaz6CPBytCueX6RIiFujcIkjlbfn9'
    access_token_secret = 'sPSKf58bPjpAwS25jHim8P7zIIxTXjZ41l5BsvKgW2nP6'
    consumer_key = 'rDJ4Mc4jL43N6V3cg4q37gpON'
    consumer_secret = 'WlWJIMkx3lEVvhKzF4SsZTK1VV8kuLGDG740tQmUO0zTujH7JD'
    search="#bigdata"
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=[search])        
