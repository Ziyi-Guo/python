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
		data = {}
		book = xlrd.open_workbook(self.source)
		sheet = book.sheet_by_name('student')
		for row in range(sheet.nrows):
			key = str(sheet.cell(row,0).value)
			v = []
			for col in range(1,sheet.ncols):
				v.append(sheet.cell(row,col).value)
			data[key] = v
		self.data = json.dumps(data,ensure_ascii=False,sort_keys=True)

	def write2xml(self):
		root = etree.Element('root')
		student = etree.SubElement(root,'student')
		s = u"\n\t学生信息表\n\tid : [名字，数学，语文，英语]\n"
		comment = etree.Comment(s)
		student.append(comment)
		student.text = '\n'+self.data+'\n'
		tree = etree.ElementTree(root)
		tree.write(self.dest,pretty_print=True,xml_declaration=True,encoding='utf-8')
		# print etree.tounicode(tree.getroot())

e2x = Excel2Xml('data.xls','data.xml')
e2x.extract_data()
e2x.write2xml()