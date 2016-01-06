import threading
import sqlite3
from datetime import datetime
from threading import Timer
import spotify

import SpotifyPlayer

Alarms = []
track_uri = 'spotify:track:0HJRAM7Gt9jXskuXjZeFX3'
spotify = SpotifyPlayer.SpotifyPlayer()

def playTrack(track_uri):
	spotify.play_track(track_uri)

# Short test to see if Spotify is working in combination with Timer
# t = Timer(1.0, playTrack, [track_uri])
# Alarms.append(t)
# t.start()
# time.sleep(10)
# print spotify.isPlaying()
# print Alarms

# Busy wait for spotify
# try:
#     while spotify.isPlaying():
#         pass
# except KeyboardInterrupt:
#     pass