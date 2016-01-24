#!/usr/bin/python

import sqlite3
import time
from threading import Timer
from urllib2 import Request,urlopen

from flask import Flask, render_template, flash, redirect, g

from forms import AddAlarmForm

app = Flask(__name__)
app.config.from_object('config')

def sendStateChange(key, value):
    request = Request("http://localhost:5000/API/update/{}/{}".format(key, value))
    response = urlopen(request)
    responseText = response.read()
    print responseText


# Because calling this directly on the object does not work for some magic
# reason
def play_track(track_uri, alarmID):
    # if alarm.spotify.isPlaying():
    #     alarm.spotify.stopPlaying()
    # alarm.spotify.play_track(track_uri)
    sendStateChange("Sensors:Alarms:{}".format(alarmID), "fire")
    timeBeforeAlarm = alarm.updateRow(alarmID, g.db)
    if timeBeforeAlarm > 0:
        t = Timer(timeBeforeAlarm, play_track, [track_uri, alarmID])
        alarm.runningAlarms.append(t)
        t.start()

class Alarm(object):

    runningAlarms = []
    # spotify = SpotifyPlayer.SpotifyPlayer()

    def __init__(self):
        # Manual creation of database connection due to no request
        db = sqlite3.connect("../sqlite.db")
        db.row_factory = sqlite3.Row
        alarms = db.execute("SELECT * FROM alarm WHERE repeat > 0 OR time > "+str(int(time.time()))).fetchall()

        for alarm in alarms:
            timeBeforeAlarm = self.updateRow(alarm['id'], db)
            t = Timer(timeBeforeAlarm, play_track, [alarm['track_uri'], alarm['id']])
            self.runningAlarms.append(t)
            t.start()

    def createAlarm(self, selectedTime, repeat, user, track_uri):
        g.db.execute("INSERT INTO alarm VALUES (NULL, ?, ?, ?, ?)", (selectedTime, repeat, user, track_uri))
        g.db.commit()
        alarmID = g.db.execute("SELECT id FROM alarm WHERE time = ? AND repeat = ? AND user = ? and track_uri = ?", (selectedTime, repeat, user, track_uri)).fetchone()
        t = Timer(selectedTime - time.time(), play_track, [track_uri, alarmID])
        self.runningAlarms.append(t)
        t.start()

    def updateRow(self, alarmID, db):
        tmpAlarmTime = db.execute("SELECT TIME FROM alarm WHERE ID = ?", (alarmID,)).fetchone()['time']
        tmpAlarmRep = db.execute("SELECT REPEAT FROM alarm WHERE ID = ?", (alarmID,)).fetchone()['repeat']
        
        if tmpAlarmRep > 0:
            while tmpAlarmTime < time.time():
                tmpAlarmTime = tmpAlarmTime + tmpAlarmRep

            db.execute("UPDATE alarm SET TIME=? WHERE ID=?", (tmpAlarmTime, alarmID))
            db.commit()
            return tmpAlarmTime - time.time()

        return tmpAlarmRep

    def removeAlarmByID(self, alarmID):
        g.db.execute("DELETE FROM alarm WHERE ID = ?", (alarmID,))
        g.db.commit()

    def isValidID(self, alarmID):
        res = g.db.execute("SELECT id FROM alarm WHERE ID = ?", (alarmID,)).fetchone()
        return res != None

    def getAllAlarms(self, db):
        return db.execute("SELECT * FROM alarm").fetchall()

    def printDB(self):
        print self.getAllAlarms()

    def start_stored_alarms(self):
        for alarm in self.alarms:
            print alarm

    def get_current_alarms_from_db(self):
        return g.db.execute(
            "SELECT * FROM alarm WHERE repeat > 0 OR time > "+str(int(time.time()))).fetchall()

    # def play_track(self, track_uri):
    #     spotify.play_track(track_uri)


alarm = Alarm()


def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.before_request
def before_request():
    g.db = sqlite3.connect("../sqlite.db")
    g.db.row_factory = sqlite3.Row

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route("/alarm/remove/<int:alarmID>")
def removeAlarm(alarmID):
    if alarm.isValidID(alarmID):
        flash('Alarm removed')
        alarm.removeAlarmByID(alarmID)
    else:
        flash('Alarm ID was not valid')
    return redirect('/')

@app.route("/")
def index():
    return render_template("index.html", alarms=alarm.getAllAlarms(g.db))

@app.route('/addalarm', methods=['GET', 'POST'])
def addAlarm():
    form = AddAlarmForm()
    if form.validate_on_submit():
        alarm.createAlarm(
            time.mktime(form.datetime.data.timetuple()),
            form.repeat.data,
            form.user.data,
            form.track_uri.data
        )
        flash('Alarm was added')
        return redirect('/')
    return render_template('addalarm.html', form=form)

# track_uri = 'spotify:track:0rCuRc07y6l1kPYj0JSRg5'

# Short test to see if Spotify is working in combination with Timer
# t = Timer(1.0, play_track, [track_uri])
# Alarms.append(t)
# t.start()

if __name__ == "__main__":
   # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
    # a = Alarm()
    #a.createAlarm(str(int(time.time())), str(3600), "angelo333", "some track")
    #a.createAlarm(str(int(time.time())), str(5500), "angelo222", "some track")
    # a.printDB()
    # print("**")
    # a.updateRow(1)
    #a.get_current_alarms_from_db()


