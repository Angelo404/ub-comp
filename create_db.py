#!/usr/bin/python

import sqlite3

sqlite_file = 'src/sqlite.db'    # name of the sqlite database file

alarmtable = '''CREATE TABLE `alarm` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`time`	NUMERIC NOT NULL,
	`repeat`	INTEGER NOT NULL,
	`user`	TEXT,
	`track_uri`	TEXT
);'''



db = sqlite3.connect(sqlite_file)
c = db.cursor()
c.execute(alarmtable)
db.commit()
db.close()