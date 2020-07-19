import sys
from pytube import YouTube
# pip install pytube3

## Test URL: pjr1pDnmOjQ

try:
	token = sys.argv[1]
	start = int(sys.argv[2])
	end = int(sys.argv[3])
except:
	print('Usage: %s <token> <start_seconds> <end_seconds>')
	sys.exit(1)

print('Downloading %s...' % (token))

raw_filename = "%s_raw" % (token)
cut_filename = "%s_cut.mp4" % (token)

yt = YouTube('http://youtube.com/watch?v=' + token)
stream = yt.streams.filter(only_audio = True, subtype = 'mp4').first()
stream.download(filename = raw_filename)
title = stream.player_config_args["title"]
thumbnail = yt.thumbnail_url
author = yt.author

print('Trimming %s...' % (token))

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("%s.mp4" % (raw_filename), start, end, targetname = cut_filename)

print(thumbnail)