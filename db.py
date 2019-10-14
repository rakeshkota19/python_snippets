

import pymysql;
import os
import sys

class DbConnection():

	def __init__(self,user_name, password, db_name):
		self.db_host = "localhost"
		self.db_user = user_name
		self.db_password = password
		self.db_port = 3306
		self.db_name = db_name

	def create_connection(self):
		conn = pymysql.connect(host = self.db_host, port = self.db_port, user = self.db_user, password = self.db_password,  db = self.db_name)
		return conn


	def run_query(self, conn, query):

		cur = conn.cursor()
		cur.execute(query)

		print(cur.fetchall())

db_instance = DbConnection(sys.argv[1], sys.argv[2], sys.argv[3])
conn = db_instance.create_connection()

db_instance.run_query(conn, "SELECT * from practise")

if(conn):
	print(os.getcwd())
