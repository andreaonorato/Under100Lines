from googleapiclient.discovery import build

# API key
api_key = "yourapikey"

# YouTube video ID
video_id = input("Enter YouTube video ID: ")

# Creating a YouTube resource object
youtube = build('youtube', 'v3', developerKey=api_key)

# Requesting comments from the video
comments = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    textFormat='plainText'
).execute()

# Printing comments and authors
for comment in comments['items']:
    author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
    text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
    print(f"Author: {author}\nComment: {text}\n")
