#!/usr/bin/python

import sqlite3

sqlite_file = 'src/sqlite.db'    # name of the sqlite database file

alarmtable = '''CREATE TABLE alarm
       (id INT PRIMARY KEY     NOT NULL,
       	time TEXT NOT NULL,
       	repeat TEXT NOT NULL,
       	user TEXT NOT NULL,
       	track_uri TEXT
       );'''



db = sqlite3.connect(sqlite_file)
c = db.cursor()
c.execute(alarmtable)
c.commit()
c.close()