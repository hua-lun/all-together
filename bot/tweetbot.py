from datetime import datetime as dt
from googleapiclient.discovery import build
import json
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
yt = build('youtube', 'v3', developerKey=YT_API_KEY)

counter = 0
data = data = json.load(open('vidCats.json'))
arr = ['1', '2', '10', '15', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
       '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44']

print(counter)


def getVid(id):
    request = yt.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode="US",
        videoCategoryId=str(id),
        maxResults=1
    )
    response = request.execute()
    return response


def tweeting():
    print('tweets...', flush=True)

    video = getVid(arr[counter])
    videoInfo = video['items'][0]["snippet"]

    title = videoInfo["title"]
    time = videoInfo["publishedAt"]

    channel = videoInfo["channelTitle"]

    stats = video['items'][0]["statistics"]["viewCount"]

    output = f"Title: {title}\nViews: {stats}\nChannel: {channel}\nPublished: {time}"

    tt = f"Live from the Raspberry Pi: it is {dt.now()}. \nCategory: {data[arr[counter]]} \n{output}"
    api.update_status(tt)
    print('success')


def startingTweet():
    print("starting")

    cats = []

    request = yt.videos().list(
        part="snippet",
        chart="mostPopular",
        regionCode="US",
        maxResults=3
    )
    response = request.execute()
    arr = response["items"]

    for i in range(0, len(arr)):
        catId = arr[i]["snippet"]["categoryId"]
        cat = data[catId]
        cats.append(cat)

    c = str(cats)
    strCats = c.replace("[", "").replace("]", "").replace("'", "")
    output = f"Bot is live. Today, videos in these categories do well: {strCats}. \nConsider creating videos relating to them!"

    api.update_status(output)


try:
    startingTweet()
except tweepy.error.TweepError:
    pass

while True:
    print(f'here {counter}')
    tweeting()
    counter += 1
    time.sleep(30)

