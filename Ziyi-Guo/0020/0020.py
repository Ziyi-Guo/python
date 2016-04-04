# coding=UTF-8
import xlrd
'''
Assignment: read xls file and sum up one col data
methods: xlrd to read data
'''

class TimeCounter():
	"""docstring for TimeCounter"""
	def __init__(self, f_name):
		self.f_name = f_name

	def count_time(self):
		wb = xlrd.open_workbook(self.f_name)
		sheet = wb.sheet_by_index(0)
		sum = 0
		p_in = 0
		p_out = 0
		for row in range(1,sheet.nrows):
			d = int(sheet.cell(row,3).value)
			sum += d
			if sheet.cell(row,2).value == u"被叫":
				p_in += d
			else:
				p_out += d
		print '总通话时间为',sum,'秒,其中呼入',p_in,'秒,呼出',p_out,'秒'

tc = TimeCounter('src.xls')
tc.count_time()
