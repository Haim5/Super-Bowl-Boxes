import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import time

spreadsheet_name = ""
secret_key_path = ""

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(secret_key_path, scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open(spreadsheet_name)
sheet = workbook.sheet1

names = []
locations = set()

digits1 = [i for i in range(10)]
digits2 = [i for i in range(10)]

random.shuffle(digits1)
random.shuffle(digits2)

for i in range(3, 13):
    sheet.update_cell(2, i, digits1.pop())
    sheet.update_cell(i, 2, digits2.pop())

for i in range(3, 13):
    for j in range(3, 13):
        locations.add((i,j))

cells = sheet.range('C3:L12')
for cell in cells:
    name = cell.value
    if name is not None and len(name) > 0:
        names.append(name)
        locations.remove((int(cell.row), int(cell.col)))
  
available_locations = list(locations)
random.shuffle(available_locations)
multiply_factor = (100 // len(names)) - 1

for _ in range(multiply_factor):
    for name in names:
        (r, c) = available_locations.pop()
        sheet.update_cell(r, c, name)
        time.sleep(0.5)

print("DONE.")
