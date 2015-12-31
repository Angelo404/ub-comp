import time
import threading
from threading import Timer

import spotify

import SpotifyPlayer

Alarms = []
track_uri = 'spotify:track:0HJRAM7Gt9jXskuXjZeFX3'

def playTrack(track_uri):
	spotify.play_track(track_uri)


spotify = SpotifyPlayer.SpotifyPlayer()
# playTrack(track_uri)
t = Timer(1.0, playTrack, [track_uri])
Alarms.append(t)
t.start()
time.sleep(10)
print spotify.isPlaying()
print Alarms


try:
    while spotify.isPlaying():
        pass
except KeyboardInterrupt:
    pass

print '\nshutdown succesful'