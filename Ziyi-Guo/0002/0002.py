import sqlite3
from RandomStringGenerator import RandomStringGenerator

# a = RandomStringGenerator()
# a.generate_strings()
# print a.list

class Database():
	def __init__(self,db_name='Test.db',tb_name='KEYS'):
		self.con = sqlite3.connect(db_name)
		self.con.execute('drop table if exists %s' %tb_name)
		self.tb_name = tb_name
		self.create_table()

	def create_table(self):
		command = '''Create table %s
					(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
					CODE TEXT NOT NULL)''' % self.tb_name
		self.con.execute(command)
		self.con.commit()
		print "JOB DONE"

	def write_data(self,data_lsit):
		for data in data_lsit:
			# pay great attention on the \' around text
			self.con.execute('INSERT INTO %s (CODE) VALUES (\'%s\')' %(self.tb_name,data))
		self.con.commit()


rsg = RandomStringGenerator()
rsg.generate_strings()
db = Database()
db.write_data(rsg.list)
# cursor = db.con.execute('SELECT * FROM %s' %db.tb_name)
# for c in cursor:
# 	print c[0],'\n',c[1]
db.con.close()