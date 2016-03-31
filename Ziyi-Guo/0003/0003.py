from RandomStringGenerator import RandomStringGenerator
import redis

class Database_R():
	def __init__(self,pt=6379,db=0):
		self.con = redis.StrictRedis(host='localhost',port=pt,db=0)

	def write_data(self,data_list,list_name):
		self.con.lpush(list_name,*data_list)
		print self.con.lrange(list_name,0,-1)

rsg = RandomStringGenerator()
rsg.generate_strings()

dbr = Database_R()
dbr.write_data(rsg.list,'mylist')