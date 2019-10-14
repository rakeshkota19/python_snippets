import mysql.connector
import sys
import os

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "12345678"
	)

print(mydb)

cursor = mydb.cursor()
