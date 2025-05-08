from openpyxl import load_workbook

workbook = load_workbook('sample.xlsx')
sheet = workbook.active

sheet['B2'] = 26

workbook.save('sample.xlsx')
print('Excel File updated successfully!')