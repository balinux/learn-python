from dataclasses import dataclass
from unittest import result
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="moodle"
)

c = mydb.cursor()

c.execute("select * from mdl_user")

result = c.fetchall()

for x in result:
    print(x)