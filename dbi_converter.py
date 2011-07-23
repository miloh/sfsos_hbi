# python yo



from xlrd import *
from sqlalchemy import *
import os
import glob

# parse directory wiwth *.xls files and iterate to open workbooks, convert to sql format  (all columns to a table exicept for the messy 'description' colum)

#  OK 
path = './'

for infile in glob.glob(os.path.join(path,'*.xls')):
 print infile
wb = open_workbook('June2009Issued_Permits.xls')
#wb = open_workbook('November2008issued_permits.xls')

#  decomment for inline thiing of all *.xls in a directory
#wb = open_workbook(inline)
      
#for s in  wb.sheets():
#      	 print 'Sheet:',s.name
#      	 for row in range(s.nrows):
#      			values = []
#      			for col in range(s.ncols):
#      					values.append(s.cell(row,col).value)
#      			print ','.join(values)
#         print



