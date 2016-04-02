import WordsCounter,os

def iter_dir(dir_name):
	file_list = [x for x in os.listdir(dir_name) if x.endswith('txt')]
	for f_name in file_list:
		wc = WordsCounter.WordsCounter(dir_name+f_name)
		wc.words_count()
		print "Belongs to \'%s\',\nthe most repetive two words: %s" %(dir_name+f_name,wc.counter[0:2])

iter_dir('test/')