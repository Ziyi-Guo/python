'''
Assignment: Replace the banned words with Good
Method: none
'''

def replace_words(sen):
	f = open('filtered_words.txt')
	ban_list = f.read().split('\n')
	f.close()
	if sen == 'exit':
		exit()
	else:
		for b in ban_list:
			if b in sen:
				sen = sen.replace(b,'**')
		print sen

while True:
	sen = raw_input('>')
	replace_words(sen)
