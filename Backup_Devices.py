import xlrd
import os.path
from Date_Time import Current_Year, Current_Month, Current_Date
from Backup_script import Running_config_Backup
from getpass import getpass
from File_Manager import isWritable, isFileAvailable

date_path = f'./{Current_Year()}/{Current_Month()}/{Current_Date()}'

template_book = xlrd.open_workbook("MyDevicesUploadTemplate.xls")
template_sheet = template_book.sheet_by_name('MyDevicesUploadTemplate')
number_of_rows = template_sheet.nrows

# Collecting Tittle cell details from excel template
Tittle_cell0 = template_sheet.cell(0, 0).value  # Device_location
Tittle_cell1 = template_sheet.cell(0, 1).value  # Serial Number
Tittle_cell2 = template_sheet.cell(0, 2).value  # Device_Name_or_Hostname
Tittle_cell3 = template_sheet.cell(0, 3).value  # Device_type
Tittle_cell4 = template_sheet.cell(0, 4).value  # IP_address
Tittle_cell5 = template_sheet.cell(0, 5).value  # Software_Version
Tittle_cell6 = template_sheet.cell(0, 6).value  # Model Number
Tittle_cell7 = template_sheet.cell(0, 7).value  # Access_Method

print(f'Please enter authentication details for template book "MyDevicesUploadTemplate"')
print(f'"MyDevicesUploadTemplate" need to placed with this app folder')

in_username = input("Enter User Name : ")
in_password = getpass(prompt="Enter Password :", stream=None)

'''
print(date_path)
print("Logging Info : Checking for file permissions " + date_path)
if not isWritable(date_path):
    print("PermissionError: Backup script do not have sufficient permission to make directory or file")

else:
'''
for x in range(1, number_of_rows):
    # Making Temporary directory from each line of the template
    temp_dict = {Tittle_cell0: template_sheet.cell(x, 0).value, Tittle_cell1: template_sheet.cell(x, 1).value,
                 Tittle_cell2: template_sheet.cell(x, 2).value, Tittle_cell3: template_sheet.cell(x, 3).value,
                 Tittle_cell4: template_sheet.cell(x, 4).value, Tittle_cell5: template_sheet.cell(x, 5).value,
                 Tittle_cell6: template_sheet.cell(x, 6).value}

    backup_path = f'{date_path}/{temp_dict[Tittle_cell0]}'

    # is path available
    if os.path.exists(backup_path):
        print("Logging Info : Backup Folder Already Available")
        if isFileAvailable(backup_path, temp_dict[Tittle_cell2]):
            print(f"\nLogging Info : {temp_dict[Tittle_cell2]} {temp_dict[Tittle_cell4]} Backup is already "
                  f"successfully done")
        else:
            Running_config_Backup(temp_dict[Tittle_cell3], temp_dict[Tittle_cell4], in_username, in_password,
                                  backup_path, temp_dict[Tittle_cell2])

    # If path is not available, creating folders, Suborders and  creating a new.txt file inside the folder to test
    else:
        os.makedirs(backup_path)
        print(f"Logging Info : New Backup Folders Created '{backup_path}' ")
        Running_config_Backup(temp_dict[Tittle_cell3], temp_dict[Tittle_cell4], in_username, in_password,
                              backup_path,
                              temp_dict[Tittle_cell2])
