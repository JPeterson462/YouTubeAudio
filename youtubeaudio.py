import sys
from pytube import YouTube
# pip install pytube3

## Test URL: pjr1pDnmOjQ

token = sys.argv[1]
yt = YouTube('http://youtube.com/watch?v=' + token)
stream = yt.streams.filter(only_audio = True, subtype = 'mp4').first()
stream.download()
title = stream.player_config_args["title"]
thumbnail = yt.thumbnail_url
author = yt.author
