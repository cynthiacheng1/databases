import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="escuela.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#creatin table
peoples_table = ("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
c.execute(peoples_table)
#adding to table
peeps = csv.DictReader(open("peeps.csv"))
for row in peeps:
	add_row = 'INSERT INTO peeps VALUES ("' + row["name"] + '",' + row["age"] + "," + row["id"] + ")"
	c.execute(add_row)

#creatin table
courses_table = "CREATE TABLE courses (code TEXT, mark NUMERIC, id NUMERIC)"
c.execute(courses_table)
#adding to table
courses = csv.DictReader(open("courses.csv"))
for row in courses:
	add_row = "INSERT INTO courses VALUES ('" + row["code"] + "'," + row["mark"] + "," + row["id"] + ")"
	c.execute(add_row)

db.commit() #save changes
db.close()  #close database
