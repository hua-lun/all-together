from googleapiclient.discovery import build
from keys import *

youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode="US",
        maxResults=3
    )

response = request.execute()

print(response)