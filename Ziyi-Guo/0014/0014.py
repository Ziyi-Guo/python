import json,xlwt
'''
Assignment: get data from txt file and write it into excel
Methods: using json to get data into dict
'''

class Data4Txt2Excel():
	def __init__(self,source,dest):
		with open(source) as f:
			self.data = json.load(f)
		self.dest = dest

	def write_into_excel(self):
		wb = xlwt.Workbook()
		ws = wb.add_sheet('student')
		row=-1;
		for key in sorted(self.data):
			row += 1
			col = 0
			ws.write(row,col,key)
			for v in self.data[key]:
				col += 1
				ws.write(row,col,v)
		wb.save(self.dest)


d4t2e = Data4Txt2Excel('student.txt','data.xls')
d4t2e.write_into_excel()