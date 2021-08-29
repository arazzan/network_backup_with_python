# network_backup_with_python

Command line tool to backup network devices - Read data from a excelsheet and "Backup all the devices" or "Filtered from the sheet and backup".

Screenshots and Deatils: 

https://e-booksnetworking.blogspot.com/2020/10/back-up-your-network-devices-with-excel.html
                         
https://e-booksnetworking.blogspot.com/2020/10/automate-your-network-device-backup.html

Modifiy the MyDeviceUploadTemplate.xls file with device inventory

2. Run the application 

           > py Backup_Devices.py
           
           it will promt for device SSH/TELNET authentication details (Username: , Password:)
           it will start the backup process. 
           Backup files will be stored in "Base DIR"\Current Year\Current Month\Date\Location Name  Ex: \2020\October\22\2nd_floor_it_room
           Device Access related loggs will be stored in Base directory (File Name Ex: Logging_22-October-2020_120604)



          
 
      
