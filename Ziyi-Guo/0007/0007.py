import os

class Code_Summary():
	"""docstring for Code_Summary"""
	def __init__(self,path='code/'):
		file_list = [path+x for x in os.listdir(path) if x.endswith('.py')]
		self.f_list = file_list

	def count_summary(self):
		sum_vol = [0,0,0]
		for f_name in self.f_list:
			f = open(f_name)
			text = f.readlines()
			f.close()
			vol_sum = len(text)
			vol_space = len([x for x in text if x.strip() == ''])
			vol_comment = len([x for x in text if x.startswith('#')])
			print 'File %s has %d lines of code,%d lines of spaces and %d lines of comment.' %(f_name,vol_sum,vol_space,vol_comment )
			sum_vol[0] += vol_sum;sum_vol[1] += vol_space;sum_vol[2] += vol_comment
		self.sum_vol = sum_vol

cs = Code_Summary()
cs.count_summary()
print "In total, %d lines of code, %d lines of space and %d lines of comment."%(cs.sum_vol[0],cs.sum_vol[1],cs.sum_vol[2])