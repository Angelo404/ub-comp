#!/usr/bin/python

from flask import Flask, render_template, flash, redirect
import sqlite3
from time import strftime
from datetime import datetime
from threading import Timer
import spotify
import SpotifyPlayer
from forms import AddAlarmForm

app = Flask(__name__)
app.config.from_object('config')

# Because calling this directly on the object does not work for some magic
# reason
def play_track(track_uri):
    alarm.spotify.play_track(track_uri)


class Alarm(object):

    #alarms = []
    #spotify = SpotifyPlayer.SpotifyPlayer()
    #db = None

    def __init__(self):
        # Needs to be replaced with something from the config file
        self.connect_to_db('../sqlite.db')
        self.c = self.db.cursor()
        #self.get_current_alarms_from_db()
        # TODO needs something to restart the timers

    def connect_to_db(self, path):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row

    def createEntry(self, time, repeat, user, track):
        self.c.execute("INSERT INTO alarm VALUES (NULL, ?, ?, ?, ?)", (time, repeat, user, track))
        self.db.commit()

    def updateRow(self, alarmID):
        self.c.execute("SELECT TIME FROM alarm WHERE ID = ?", (alarmID,))
        tmpAlarmTime = self.c.fetchone()[0]
        self.c.execute("SELECT REPEAT FROM alarm WHERE ID = ?", (alarmID,))
        tmpAlarmRep = self.c.fetchone()[0]
        self.c.execute("UPDATE alarm SET TIME=? WHERE ID=?", (tmpAlarmTime+tmpAlarmRep, alarmID))
        self.db.commit()

    def printDB(self):
        self.c.execute("SELECT * FROM alarm")
        print(self.c.fetchall())

    def start_stored_alarms(self):
        for alarm in self.alarms:
        	print alarm

    def get_current_alarms_from_db(self):
        self.alarms = self.query_db(
            "SELECT * FROM alarm WHERE repeat > 0 OR time > "+str(int(time.time())))
        self.start_stored_alarms()

    def query_db(self, query, args=(), one=False):
        cur = self.db.execute(query, args)
        rv = cur.fetchall()
        print(rv)
        cur.close()
        #return (rv[0] if rv else None) if one else rv

    def playtrack(self):
        play_track('spotify:track:0HJRAM7Gt9jXskuXjZeFX3')

    def play_track(self, track_uri):
        spotify.play_track(track_uri)

#@app.route("/")
def root():
    return render_template("home.html", alarms=alarm.alarms)

@app.route('/addalarm', methods=['GET', 'POST'])
def addAlarm():
    form = AddAlarmForm()
    if form.validate_on_submit():
        print form.track_uri.data + " " + form.user.data
        flash('"%s", %s' %
              (form.track_uri.data, str(form.user.data)))
        return redirect('/')
    return render_template('addalarm.html',
                           form=form)

# track_uri = 'spotify:track:0rCuRc07y6l1kPYj0JSRg5'
alarm = Alarm()

# Short test to see if Spotify is working in combination with Timer
# t = Timer(1.0, play_track, [track_uri])
# Alarms.append(t)
# t.start()

if __name__ == "__main__":
    #app.run(debug=True)
    a = Alarm()
    #a.createEntry(str(int(time.time())), str(3600), "angelo333", "some track")
    #a.createEntry(str(int(time.time())), str(5500), "angelo222", "some track")
    a.printDB()
    print("**")
    a.updateRow(1)
    #a.get_current_alarms_from_db()



