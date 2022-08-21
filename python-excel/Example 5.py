# Getting Rows and Columns from the Sheets
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
# Open an excel file in current directory
wb = openpyxl.load_workbook('file_example_XLSX_10.xlsx')

# Get active sheet
sheet = wb.active

print(tuple(sheet['A1':'C3']))
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')