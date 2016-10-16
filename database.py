#!/usr/bin/python
import sqlite3

print "We are using the SQlite DB API"


conn = sqlite3.connect('students.db')
c = conn.cursor()

all_rows = c.fetchall()
print(all_rows)
