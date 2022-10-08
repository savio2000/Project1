from distutils.cmd import Command
import sqlite3
connection=sqlite3.connect("user_data.db")
cursor=connection.cursor()
# cmd="""CREATE TABLE IF NOT EXISTS login_data(name TEXT,password TEXT)"""
cursor.execute("insert into login_data values('savio','12345678')")
connection.commit()