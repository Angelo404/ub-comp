#!/usr/bin/python

import sqlite3

sqlite_file = 'src/sqlite.db'    # name of the sqlite database file

alarmtable = '''CREATE TABLE alarm
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       	TIME INT NOT NULL,
       	REPEAT INT NOT NULL,
       	USER TEXT NOT NULL,
       	TRACK_URI TEXT
       );'''



db = sqlite3.connect(sqlite_file)
c = db.cursor()
c.execute(alarmtable)
db.commit()
db.close()