#!/usr/bin/python

from flask import Flask, render_template, send_from_directory
import sqlite3
import time
from datetime import datetime
from threading import Timer
import spotify
import SpotifyPlayer

app = Flask(__name__)

# Because calling this directly on the object does not work for some magic
# reason
def play_track(track_uri):
    alarm.spotify.play_track(track_uri)


class Alarm(object):

    alarms = []
    spotify = SpotifyPlayer.SpotifyPlayer()
    db = None

    def __init__(self):
        # Needs to be replaced with something from the config file
        self.connect_to_db('../sqlite.db')
        self.get_current_alarms_from_db()
        # TODO needs something to restart the timers

    def connect_to_db(self, path):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row

    def start_stored_alarms(self):
        for alarm in self.alarms:
            Timer(1.0, play_track, [alarm['track_uri']]).start()

    def get_current_alarms_from_db(self):
        self.alarms = self.query_db(
            "SELECT * FROM alarm WHERE repeat > 0 OR time > date('now')")
        self.start_stored_alarms()

    def query_db(self, query, args=(), one=False):
        cur = self.db.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    def playtrack(self):
        play_track('spotify:track:0HJRAM7Gt9jXskuXjZeFX3')

    def play_track(self, track_uri):
        spotify.play_track(track_uri)

@app.route("/")
def root():
    return render_template("addalarm.html")

# track_uri = 'spotify:track:0rCuRc07y6l1kPYj0JSRg5'
# alarm = Alarm()

# Short test to see if Spotify is working in combination with Timer
# t = Timer(1.0, play_track, [track_uri])
# Alarms.append(t)
# t.start()

if __name__ == "__main__":
    app.run(debug=True)




