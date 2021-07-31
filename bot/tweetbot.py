import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from keys import *

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    api.update_status('This is a test')
    print('success')


reply_to_tweets()
