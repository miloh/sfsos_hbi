# python

from xlrd import *
from sqlalchemy import *
import os
import glob


# parse directory wiwth *.xls files and iterate to open workbooks, convert to sql format  (all columns to a table except for the messy description colum)

#  OK
path = '../sfdbi/'

data = {}
for infile in glob.glob(os.path.join(path,'*.xls')):
#afile = {}
#afile['filename'] = infile

# print infile
#wb = open_workbook(November2008issued_permits.xls

#  decomment for inline thing of all *.xls in a directory
 wb = open_workbook(infile)

#  wb.sheet()[0]  is the sheet object... assume there is only 1/file 
 sheet = wb.sheets()[0]
 colnames = []
 testrange = [3,6]   # add in cols 17,18,19,20,21 for address data...
 for col in testrange:     # range(sheet.ncols):
  colnames.append(sheet.cell(0, col))
 data[infile] = {'colnames': colnames}


