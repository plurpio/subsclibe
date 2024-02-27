import re, urllib, urllib.error, urllib.parse, urllib.request

def channelID(channel):
    html = (urllib.request.urlopen("https://youtube.com/@" + channel).read().decode("utf-8"))
    channel = re.search(r'href="https://www\.youtube\.com/feeds/videos\.xml\?channel_id=([^"]+)"', html)
    return channel.group(1)
