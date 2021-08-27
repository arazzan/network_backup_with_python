import sqlite3
from ExcelTemplate import ExcelTemplate

try:
    conn = sqlite3.connect('Network_Inventory_new.db')
    print("Opened database successfully")
except Error as e:
    print(e)

"Query all rows in the network_devices table and print using a for loop"

cur = conn.cursor()

cur.execute("SELECT * FROM Network_Devices")

rows = cur.fetchall()

for row in rows:
    print(row)
