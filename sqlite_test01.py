import sqlite3
from ExcelTemplate import ExcelTemplate
conn = sqlite3.connect('Network_Inventory.db')
print("Opened database successfully")

file1 = ExcelTemplate("MyDevicesUploadTemplate.xls", "MyDevicesUploadTemplate")
from_excel_sheet = file1.xl_filter()

for x in from_excel_sheet:
    conn.execute(f'''INSERT INTO Network_Devices (ID, Device_Location, Serial_Number, Hostname, IP_Address,
Software_Version, Model_Number, Access_Method) VALUES (?,?,?,?,?,?,?,?)''', x)

conn.commit()
print("Records created successfully")
conn.close()