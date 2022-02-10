from xlutils.copy import copy
import xlwt, xlrd
from constant import *


def WriteToExcel(company_info, search_keyword, index):
    data = xlrd.open_workbook('info.xls', formatting_info=True)
    excel = copy(wb=data)
    excel_table = excel.get_sheet(0)
    table = data.sheets()[0]
    excel_table.write(index, 0, index)
    excel_table.write(index, 1, search_keyword)
    excel_table.write(index, 2, company_info[STRING_ARTIFICIAL_PERSON])
    excel_table.write(index, 3, company_info[STRING_ADDRESS])

    excel.save('info.xls')
