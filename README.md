# network_backup_with_python

Screenshots and Deatils: https://e-booksnetworking.blogspot.com/2020/10/back-up-your-network-devices-with-excel.html
                         https://e-booksnetworking.blogspot.com/2020/10/automate-your-network-device-backup.html

# Full Backup at once. (Same Authentication for all the devices)
           1. Modifiy the MyDeviceUploadTemplate.xls file with device inventory
           2. Run the application 
                      > py Backup_Devices.py
           
                      app console will promt for device SSH/TELNET authentication details (Username: , Password:)
                      app console will start the backup process. 
                      Backup files will be stored in "Base DIR"\Current Year\Current Month\Date\Location Name  Ex: \2020\October\22\2nd_floor_it_room
                      Device Access related loggs will be stored in Base directory (File Name Ex: Logging_22-October-2020_120604)

# Selected/Filters list of device backup
           1. run the application
                      > py filtered_backup.py
                      filter can be done based on excel sheet colum and row
                               
                       Option1 = [Device_Location,
                                  Serial_Number,
                                  Device_Name_or_Hostname,
                                  Device_type,
                                  IP_address,
                                  Software_Version,
                                  Model Number,
                                  Access_Method,
                                  ]
                       
                       Ex: Option2 = [Telnet,
                                      SSH,
                                      ]
                                 
               
                      app console will promt for device SSH/TELNET authentication details (Username: , Password:)
                      app console will start the backup process. 
                      Backup files will be stored in "Base DIR"\Current Year\Current Month\Date\Location Name  Ex: \2020\October\22\2nd_floor_it_room
                      Device Access related loggs will be stored in Base directory (File Name Ex: Logging_22-October-2020_120604)
           
                    


 
      
