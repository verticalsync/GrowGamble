import sqlite3


class User:
	def __init__(self, id: int, user_id: int, balance: int, wagered: int, highest_balance: int, growid: str, conn: sqlite3.Connection = None) -> None:
		self.__id = id
		self.__user_id = user_id
		self.__balance = balance
		self.__wagered = wagered
		self.__highest_balance = highest_balance
		self.__growid = growid
		self.__conn = conn
		self.__cursor = conn.cursor() if self.__conn else None

		if self.get_balance() > self.get_highest_balance():
			self.set_highest_balance(self.get_balance())

	def get_connection(self) -> sqlite3.Connection | None:
		return self.__conn

	def get_cursor(self) -> sqlite3.Cursor | None:
		return self.__cursor

	def get_id(self) -> int:
		return self.__id

	def get_user_id(self) -> int:
		return self.__user_id

	def get_balance(self) -> int:
		return self.__balance

	def get_wagered(self) -> int:
		return self.__wagered

	def get_highest_balance(self) -> int:
		return self.__highest_balance

	def get_growid(self) -> str:
		return self.__growid

	def set_balance(self, amount: int):
		self.__cursor.execute(f"UPDATE users SET balance = {amount} WHERE user_id = {self.__user_id}")
		self.__conn.commit()
		self.__balance = amount
		return

	def set_wagered(self, amount: int):
		self.__cursor.execute(f"UPDATE users SET wagered = {amount} WHERE user_id = {self.__user_id}")
		self.__conn.commit()
		self.__wagered = amount
		return

	def set_highest_balance(self, amount: int):
		self.__cursor.execute(f"UPDATE users SET highest_balance = {amount} WHERE user_id = {self.__user_id}")
		self.__conn.commit()
		self.__highest_balance = amount
		return

	def set_growid(self, growid: str) -> bool:
		sql = f"SELECT * FROM users WHERE linked_growid LIKE '{growid}'"
		res = self.__cursor.execute(sql).fetchone()
		if not res:
			self.__cursor.execute(f"UPDATE users SET linked_growid = '{growid}' WHERE user_id = {self.__user_id}")
			self.__conn.commit()
			self.__growid = growid
			return True
		else:
			return False

	def wipe(self):
		self.set_highest_balance(0)
		self.set_wagered(0)
		self.set_balance(0)
		self.set_growid("")


class Database:
	def __init__(self, database_file_name) -> None:
		self.__conn = None
		self.__cursor = None
		self.__connect(database_file_name)

	def __connect(self, database_file_name: str):
		self.__conn = sqlite3.connect(database_file_name)
		self.__cursor = self.__conn.cursor()

	def disconnect(self):
		if self.__conn:
			self.__conn.close()
			self.__conn = None
			self.__cursor = None

	def get_connection(self) -> sqlite3.Connection | None:
		return self.__conn

	def get_cursor(self) -> sqlite3.Cursor | None:
		return self.__cursor

	def register(self, user_id: int):
		if self.__conn:
			self.__cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
				(None, user_id, 0, 0, 0, ""))  # id, user_id, balance, wagered, highest_balance, linked_growid
			self.__conn.commit()

	def get_user(self, user_id: int) -> User:
		if self.__conn:
			sql = f"SELECT * FROM users WHERE user_id LIKE {user_id}"
			res = self.__cursor.execute(sql).fetchone()
			if not res:
				self.register(user_id)
				res = self.__cursor.execute(sql).fetchone()
			return User(res[0], res[1], res[2], res[3], res[4], res[5], self.__conn)

	def get_user_by_id(self, id: int) -> User | None:
		if self.__conn:
			sql = f"SELECT * FROM users WHERE id LIKE {id}"
			res = self.__cursor.execute(sql).fetchone()
			if not res:
				return None
			return User(res[0], res[1], res[2], res[3], res[4], res[5], self.__conn)

	def get_user_by_growid(self, growid: str) -> User | None:
		if self.__conn:
			sql = f"SELECT * FROM users WHERE linked_growid LIKE '{growid}'"
			res = self.__cursor.execute(sql).fetchone()
			if not res:
				return None
			return User(res[0], res[1], res[2], res[3], res[4], res[5], self.__conn)

	def get_users(self) -> list[User]:
		if self.__conn:
			users = []
			sql = f"SELECT * FROM users"
			res = self.__cursor.execute(sql).fetchall()
			for resp in res:
				users.append(User(resp[0], resp[1], resp[2], resp[3], resp[4], resp[5], self.__conn))
			return users
