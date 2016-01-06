import sqlite3

sqlite_file = 'src/sqlite.db'    # name of the sqlite database file

alarmtable = '''insert into alarm (time, repeat, user, track_uri) values \
('2016-02-01 02:34:56', -1, 'user', 'sometrackuri')'''

db = sqlite3.connect(sqlite_file)
c = db.cursor()
c.execute(alarmtable)
c.commit()
c.close