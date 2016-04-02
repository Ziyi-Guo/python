from HTMLParser import HTMLParser
'''
Assignment: Find content from a html file
Method: maybe with htmlparser, 
'''

class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		if tag == 'a':
			for name,value in attrs:
				if name == 'href':
					print name,'=',value

f = open('c.html')
text = f.read()
f.close()
mhp = MyHTMLParser()
mhp.feed(text)