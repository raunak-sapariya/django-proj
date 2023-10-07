""" 
import requests
from youtube_transcript_api import YouTubeTranscriptApi 



def searchYoutube(query):
    data=requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyB00x-Q36iveVfeFnn8EF95_FiURsH4AuQ&q="+query)
    data=data.json()
    return data["items"][0].id.videoId



def getSubtitle(id):
    script=YouTubeTranscriptApi.get_transcript(id) """