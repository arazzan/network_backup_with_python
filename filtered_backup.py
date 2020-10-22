import xlrd
import os.path
from Date_Time import Current_Year, Current_Month, Current_Date
from Backup_script import Running_config_Backup
from getpass import getpass
from File_Manager import isWritable, isFileAvailable
from ExcelTemplate import ExcelTemplate
from collections import OrderedDict
from collections import namedtuple
import prettytable

date_path = f'./{Current_Year()}/{Current_Month()}/{Current_Date()}'

print(f'Welcome to Network device Backup with Python"')
print(" ")
print(f'"MyDevicesUploadTemplate" is the device inventory file, it need to be modified with device details')
print(" ")
print(f'"MyDevicesUploadTemplate" file need to placed with this app base folder')
print(" ")
print(f'Please select the devices to start the backup"')

file1 = ExcelTemplate("MyDevicesUploadTemplate.xls", "MyDevicesUploadTemplate")
readable_table = prettytable.PrettyTable(file1.Title_row_dict().values())
filtered_list = file1.xlFilter()


# print(filtered_list)
for x in filtered_list:
    readable_table.add_row(x)
print(readable_table)

print(" ")
print(f'Please enter authentication details for selected devices')
in_username = input("Enter User Name : ")
in_password = getpass(prompt="Enter Password :", stream=None)

for device in filtered_list:
    backup_path = f'{date_path}/{device[0]}'

    # is path available
    if os.path.exists(backup_path):
        print("Logging Info : Backup Folder Already Available")
        if isFileAvailable(backup_path, device[2]):
            print(f"\nLogging Info : {device[2]} {device[4]} Backup is already "
                  f"successfully done")
        else:
            Running_config_Backup(device[3], device[4], in_username, in_password,
                                  backup_path, device[2])

    # If path is not available, creating folders, Suborders and  creating a new.txt file inside the folder to test
    else:
        os.makedirs(backup_path)
        print(f"Logging Info : New Backup Folders Created '{backup_path}' ")
        Running_config_Backup(device[3], device[4], in_username, in_password,
                              backup_path, device[2])

date_path = f'./{Current_Year()}/{Current_Month()}/{Current_Date()}'



'''
print(date_path)
print("Logging Info : Checking for file permissions " + date_path)
if not isWritable(date_path):
    print("PermissionError: Backup script do not have sufficient permission to make directory or file")

else:
'''
# for x in range(1, number_of_rows):
#     # Making Temporary directory from each line of the template
#     temp_dict = {Tittle_cell0: template_sheet.cell(x, 0).value, Tittle_cell1: template_sheet.cell(x, 1).value,
#                  Tittle_cell2: template_sheet.cell(x, 2).value, Tittle_cell3: template_sheet.cell(x, 3).value,
#                  Tittle_cell4: template_sheet.cell(x, 4).value, Tittle_cell5: template_sheet.cell(x, 5).value,
#                  Tittle_cell6: template_sheet.cell(x, 6).value}


