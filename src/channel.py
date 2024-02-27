"Stuff related to channels"
import re
import urllib
import urllib.error
import urllib.parse
import urllib.request


def channelID(channel):
    '''Takes in channel shortname (without @) and outputs it's channel ID'''
    html = (urllib.request.urlopen("https://youtube.com/@" + channel).read().decode("utf-8"))
    channel = re.search(r'href="https://www\.youtube\.com/feeds/videos\.xml\?channel_id=([^"]+)"', html)
    return channel.group(1)
