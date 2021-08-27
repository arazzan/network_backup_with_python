import sqlite3
from ExcelTemplate import ExcelTemplate

conn = sqlite3.connect('Network_Inventory_new1.db')
print("Opened database successfully")

file1 = ExcelTemplate("MyDevicesUploadTemplate.xls", "MyDevicesUploadTemplate")
from_excel_sheet = file1.xlFilter()

# Creating table as per requirement
sql = '''CREATE TABLE IF NOT EXISTS Network_Devices(ID INT, 
                                      Device_Location CHAR(20) NOT NULL,
                                      Serial_Number CHAR(20) NOT NULL,
                                      Hostname CHAR(20) NOT NULL,
                                      IP_Address CHAR(20) NOT NULL UNIQUE,
                                      Software_Version CHAR(20) NOT NULL,
                                      Model_Number CHAR(20) NOT NULL,
                                      Access_Method CHAR(20) NOT NULL)'''

conn.execute(sql)
for x in from_excel_sheet:
    print(x)
    try:
        conn.execute(f'INSERT INTO Network_Devices (ID, Device_Location, Serial_Number, Hostname, IP_Address, '
                     f'Software_Version, Model_Number, Access_Method) VALUES (?,?,?,?,?,?,?,?)', x)
        conn.commit()
        print("Records created successfully")

    except sqlite3.IntegrityError:
        print("Records already available in DB")


conn.close()
