# Load an exal file and get an active sheet

import openpyxl

# Open an excel file in current directory
wb = openpyxl.load_workbook('file_example_XLSX_10.xlsx')

# type of file
print("Type: ", type(wb))

# get sheets in current excel file
print("Sheets:\n", wb.sheetnames)

# select a specific sheet
sheet = wb['Sheet1']
print("Selected sheet:\n",sheet)

# type of selected sheet
print("Type of selected sheet : \n", type(sheet))

# Title of selected sheet
print("Title of sheet:\n",sheet.title)

# Get active sheet
anotherSheet = wb.active
print("Active sheet in excel file:\n", anotherSheet)
