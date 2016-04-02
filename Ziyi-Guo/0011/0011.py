'''
Assignment: Replace the banned words with Good
Method: none
'''

def replace_words(word):
	f = open('filtered_words.txt')
	ban_list = f.read().split('\n')
	f.close()
	if word == 'exit':
		exit()
	elif word in ban_list:
		print "Freedom"
	else:
		print "Human Rights"

while True:
	word = raw_input('>')
	replace_words(word)
