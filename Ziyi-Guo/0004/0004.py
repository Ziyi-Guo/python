import re,operator

class WordsCounter():
	def __init__(self,file_name):
		f = open(file_name)
		text = str(f.readlines())
		f.close()
		self.words_list = [x for x in re.split('\W+',text) if len(x)>0]

	def words_count(self):
		counter = {}
		for x in self.words_list:
			if x not in counter.keys():
				counter[x] = 1
			else:
				counter[x] += 1
		self.counter = sorted(counter.items(),key=operator.itemgetter(1),reverse=True)
		print self.counter

wc = WordsCounter('RandomStringGenerator.py')
wc.words_count()