# python yo



from xlrd import *
from sqlalchemy import *


# parse directory wiwth *.xls files and iterate to open workbooks, convert to sql format  (all columns to a table except for the messy 'description' colum)
wb = open_workbook('June2009Issued_Permits.xls')

for s in  wb.sheets():
	 print 'Sheet:',s.name
	 for row in range(s.nrows):
			values = []
			for col in range(s.ncols):
					values.append(s.cell(row,col).value)
			print ','.join(values)
	  print
