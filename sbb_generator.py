import gspread
from gspread.utils import rowcol_to_a1
from oauth2client.service_account import ServiceAccountCredentials
import random

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

cells_to_update = []
formats_to_update = []

for _ in range(multiply_factor):
    for name in names:
        (r, c) = available_locations.pop()
        cells_to_update.append(gspread.Cell(r, c, name))
        formats_to_update.append({"range": rowcol_to_a1(r, c), "format": {"backgroundColor": {"red": 1.0, "green": 1.0, "blue": 0.0}}})

if cells_to_update:
    sheet.update_cells(cells_to_update)
    sheet.batch_format(formats_to_update)

digits1 = [i for i in range(10)]
digits2 = [i for i in range(10)]

random.shuffle(digits1)
random.shuffle(digits2)

digits_cells = []
for i in range(3, 13):
    digits_cells.append(gspread.Cell(2, i, digits1.pop()))
    digits_cells.append(gspread.Cell(i, 2, digits2.pop()))

sheet.update_cells(digits_cells)

print("DONE.")
