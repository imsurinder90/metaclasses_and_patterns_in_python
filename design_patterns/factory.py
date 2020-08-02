"""
Factory pattern lets you register a number of classes
by assigning class object to its attribues 'db_name'
in ConnectionMeta class. For example
Factory pattern helps adding support of multiple
databases for an application. If application needs
a connection of PostgreSQL database, It passes its
name to Factory's method which returns respective
database connection object.
"""

class ConnectionMeta(type):
	"""
	This metaclass creates cls object and 
	registers each class linked to it and stores
	into its dictionary.
	"""
	def __new__(cls, clsname, bases, clsdict):
		clsobj = super().__new__(cls, clsname, bases, clsdict)
		if clsname != "Connection":
			# Bind each db type class with ConnectionMeta class
			setattr(cls, clsdict['db_name'], clsobj)
		return clsobj

class Connection(metaclass=ConnectionMeta):
	
	def connect(self, *args, **kwargs):
		pass

	def disconnect(self):
		pass

class Oracle(Connection):
	db_name = 'Oracle'

	def __init__(self, host, port, username, password):
		self.host = host
		self.port = port
		self.username = username
		self.password = password

	def __str__(self):
		return "Oracle db connection"

class PostgreSQL(Connection):
	db_name = 'PostgreSQL'

	def __init__(self, host, port, username, password):
		self.host = host
		self.port = port
		self.username = username
		self.password = password
	
	def __str__(self):
		return "PostgreSQL db connection"

class Factory:
	def get_db(db_name):
		return ConnectionMeta.__dict__[db_name]

def main():
	"""
	>>> oracle_cls = Factory.get_db('Oracle')
	>>> oracle_obj = oracle_cls(host="localhost", port=4543, username="test", password="test123")
	>>> print(oracle_obj.__dict__)
	{'host': 'localhost', 'port': 4543, 'username': 'test', 'password': 'test123'}
	"""

if __name__ == "__main__":
	import doctest
	doctest.testmod()
