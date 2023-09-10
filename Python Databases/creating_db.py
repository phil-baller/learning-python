import sqlite3

conn = sqlite3.connect('new_data.sqlite')
run = conn.cursor()

#run.execute('DROP TABLES IF EXISTS Tracks')
run.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
run
conn.close()