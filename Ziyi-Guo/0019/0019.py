 # coding=UTF-8
import xlrd,json
from lxml import etree
'''
Assignment: read data from xls and write into xml
Methods: xlrd to read data, lxml to write data 
'''

class Excel2Xml():
	def __init__(self,source,dest):
		self.source = source
		self.dest = dest

	def extract_data(self):
		data = []
		book = xlrd.open_workbook(self.source)
		sheet = book.sheet_by_index(0)
		for row in range(sheet.nrows):
			v = []
			for col in range(0,sheet.ncols):
				v.append(int(sheet.cell(row,col).value))
			data.append(v)
		self.data = json.dumps(data,ensure_ascii=False)

	def write2xml(self):
		root = etree.Element('root')
		student = etree.SubElement(root,'numbers')
		s = u"\n\t数字信息\n"
		comment = etree.Comment(s)
		student.append(comment)
		student.text = '\n'+self.data+'\n'
		tree = etree.ElementTree(root)
		tree.write(self.dest,pretty_print=True,xml_declaration=True,encoding='utf-8')
		# print etree.tounicode(tree.getroot())

e2x = Excel2Xml('numbers.xls','numbers.xml')
e2x.extract_data()
e2x.write2xml()
