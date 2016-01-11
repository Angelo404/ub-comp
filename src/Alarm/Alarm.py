#!/usr/bin/python

import threading
import sqlite3
import time
from datetime import datetime
from threading import Timer
import spotify

import SpotifyPlayer

class Alarm(object):

	alarms = []
	spotify = SpotifyPlayer.SpotifyPlayer()
	db = None 

	def __init__(self):
		self.connect_to_db('../sqlite.db') # Needs to be replaced with something from the config file
		self.get_current_alarms_from_db()
		# TODO needs something to restart the timers

	def connect_to_db(self, path):
		self.db = sqlite3.connect(path)
		self.db.row_factory = sqlite3.Row

	def get_current_alarms_from_db(self):
		self.alarms = self.query_db("SELECT * FROM alarm WHERE repeat > 0 OR time > date('now')")

	def query_db(self, query, args=(), one=False):
	    cur = self.db.execute(query, args)
	    rv = cur.fetchall()
	    cur.close()
	    return (rv[0] if rv else None) if one else rv

	def playtrack(self):
		play_track('spotify:track:0HJRAM7Gt9jXskuXjZeFX3')

	def play_track(self, track_uri):
		spotify.play_track(track_uri)

# Because calling this directly on the object does not work for some magic reason
def play_track(track_uri):
	alarm.spotify.play_track(track_uri)

track_uri = 'spotify:track:0HJRAM7Gt9jXskuXjZeFX3'
alarm = Alarm()

# c = db.cursor()
# result = c.execute('''SELECT * FROM alarm WHERE repeat > 0 OR time > date('now')''')
# query = 'SELECT * FROM alarm'
# print query
# c.execute(query)
# result = c.fetchall()
# res = alarm.alarms
# for row in res:
	# print row['user']


# Short test to see if Spotify is working in combination with Timer
t = Timer(1.0, play_track, [track_uri])
# Alarms.append(t)
t.start()
time.sleep(10)
# print spotify.isPlaying()
# print Alarms

# Busy wait for spotify
try:
    while alarm.spotify.isPlaying():
        pass
except KeyboardInterrupt:
    pass
