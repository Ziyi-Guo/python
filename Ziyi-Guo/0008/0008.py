from HTMLParser import HTMLParser
'''
Assignment: Find content from a html file
Method: maybe with htmlparser, 
'''

class MyHTMLParser(HTMLParser):
	def handle_data(self,data):
		d = data.strip()
		d = d.replace('\t','')
		d = d.replace('\n','')
		if d != '':
			print d

f = open('c.html')
text = f.read()
f.close()
mhp = MyHTMLParser()
mhp.feed(text)