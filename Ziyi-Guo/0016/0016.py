import json,xlwt
'''
Assignment: get data from txt file and write it into excel
Methods: using json to get data into list
'''

class Data4Txt2Excel():
	def __init__(self,source,dest):
		with open(source) as f:
			self.data = json.load(f)
		self.dest = dest

	def write_into_excel(self):
		wb = xlwt.Workbook()
		ws = wb.add_sheet('numbers')
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				ws.write(i,j,self.data[i][j])
		wb.save(self.dest)


d4t2e = Data4Txt2Excel('numbers.txt','numbers.xls')
d4t2e.write_into_excel()