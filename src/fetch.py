"Fetching videos"

import re
import asyncio
import aiohttp

import data

async def subscriptionFetchData():
    '''Fetches RSS feeds for every channel in subscription'''
    videoList = []
    async with aiohttp.ClientSession() as session:
        for i in data.subscriptionList():
            feed = await session.get("https://www.youtube.com/feeds/videos.xml?channel_id="+i, ssl=False)
            xml = await feed.text()
            for y in xml.split("yt:video:"):
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
    return sorted(videoList, key=lambda x: x[3], reverse=True)

def subscriptionFetch():
    '''Processes data from subscriptionFetchFeeds()'''
    return asyncio.run(subscriptionFetchData())
