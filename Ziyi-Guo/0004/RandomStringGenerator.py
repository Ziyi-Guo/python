import string,random

class RandomStringGenerator():
	def __init__(self,r_vol=200,s_len=6):
		self.vol = r_vol
		self.string_len = s_len
		self.list = []

	def generate_strings(self):
		ch_list = []
		ch_list.extend(string.ascii_uppercase)
		ch_list.extend(string.ascii_lowercase)
		ch_list.extend(string.digits)
		len_ch = len(ch_list)
		for i in range(self.vol):
			tmp_index = random.sample(range(1,len_ch),self.string_len)
			self.list.append(''.join([ch_list[j] for j in tmp_index]))


# rsg = RandomStringGenerator()
# rsg.generate_strings()
# f = open('strings.txt','w')
# f.writelines([s+'\n' for s in rsg.list)
# f.close