# To access the values of cells in a particular row or column, you can also use a Worksheet object’s rows and columns attribute

import openpyxl
# Open an excel file in current directory
wb = openpyxl.load_workbook('file_example_XLSX_10.xlsx')
# Get active sheet
sheet = wb.active
for row in sheet.columns:
    for cell in row:
        print(cell.coordinate,  cell.value)
    print("----- End of Column -----")