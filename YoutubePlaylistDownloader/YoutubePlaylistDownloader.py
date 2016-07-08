#!/usr/bin/env python
#Author:Aditya kamat

import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        #Input your youtube playlisty link here
		'https://www.youtube.com/watch?v=2QJPAZMDwXk&list=PLRAV69dS1uWSa1lzXH4EtdF75TjNX_aeH',  
        download=True
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

#print(video)
video_url = video['url']
print(video_url)			
