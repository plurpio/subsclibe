import re
import urllib.error
import urllib.parse
import urllib.request
import data, channel

def channelFetch(channel):
    videoList = []
    feed = "https://www.youtube.com/feeds/videos.xml?channel_id=" + channel
    feed = urllib.request.urlopen(feed).read().decode("utf-8")
    for i in feed.split("yt:video:"):
        video = []
        
        x = re.search("<yt:videoId>(.*?)</yt:videoId>", i)  # Gets video ID
        if x: video.append(x.group(1))
        else: continue # Stops if anything else but video ID is detected
        
        x = re.search("<title>(.*?)</title>", i)  # Gets video name
        if x: video.append(x.group(1))
        
        x = re.search("<name>(.*?)</name>", i)  # Gets video author
        if x: video.append(x.group(1))
        
        x = re.search("<published>(.*?)</published>", i)  # Gets date
        if x: video.append(x.group(1))
        
        x = re.search("<media:description>(.*?)</media:description>", i, re.DOTALL)  # Gets description
        if x: video.append(x.group(1))
        
        videoList.append(video)
    return videoList

def subscriptionFetch():
    videoList = []
    for i in data.subscriptionList():
        feed = urllib.request.urlopen("https://www.youtube.com/feeds/videos.xml?channel_id=" + channel.channelID(i)).read().decode("utf-8")
        for y in feed.split("yt:video:"):
            video = []
           
            x = re.search("<yt:videoId>(.*?)</yt:videoId>", y)  # Gets video ID
            if x: video.append(x.group(1))
            else: continue # Stops if anything else but video ID is detected
            
            x = re.search("<title>(.*?)</title>", y)  # Gets video name
            if x: video.append(x.group(1))
            
            x = re.search("<name>(.*?)</name>", y)  # Gets video author
            if x: video.append(x.group(1))
            
            x = re.search("<published>(.*?)</published>", y)  # Gets date
            if x: video.append(x.group(1))
            
            x = re.search("<media:description>(.*?)</media:description>", y, re.DOTALL)  # Gets description
            if x: video.append(x.group(1))
            
            videoList.append(video)
    return videoList
