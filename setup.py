import sqlite3

SQL = """CREATE TABLE IF NOT EXISTS users (
		id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
		user_id integer NULL,
		balance integer NULL,
		wagered integer NULL,
		highest_balance integer NULL,
		linked_growid varchar(32) NULL
		)"""

conn = sqlite3.connect("misc/database.db")
cursor = conn.cursor()
cursor.execute(SQL)
