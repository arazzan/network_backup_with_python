"""

Backup Script

"""
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException
from Date_Time import Current_Date_Time
import time
import os

today = Current_Date_Time()
logging_file = f'Logging_{today}.txt'


def Running_config_Backup(device_type, device_ip, username, password, save_path, device_name):
    try:
        print(f"\n\nStep1 : Connecting to Device {device_ip}")
        net_connect = ConnectHandler(device_type=device_type, ip=device_ip, username=username, password=password)
        net_connect.enable()
        time.sleep(1)

        print("\n\nStep2 : Reading the running config ")
        output = net_connect.send_command('show run')
        time.sleep(3)

        file_name = f'{device_name}_{device_ip}_{today}'
        full_filename = f'{os.path.join(save_path)}/{file_name}.txt'
        save_config = open(full_filename, 'w+')

        print("\n\nStep3 : Writing Configuration to file")
        save_config.write(output)
        save_config.close()
        time.sleep(2)
        net_connect.disconnect()
        print(f"\n\nStep4 : Configuration saved to file {full_filename} \n\n")

        error_log_file = open(logging_file, "a")
        error_log_file.write(f"\n{today}: backup successful for {device_name} {device_ip}")
        error_log_file.close()

    except PermissionError:
        print(f'\nPermissionError: Access Denied {save_path}')
        error_log_file = open(logging_file, "a")
        error_log_file.write(f"\n{today}: Access Denied to write in path {save_path}")
        error_log_file.close()

    except (NetMikoAuthenticationException, NetMikoTimeoutException):
        print(f"\n{today}: Authentication Error {device_name} {device_ip}")
        error_log_file = open(logging_file, "a")
        error_log_file.write(f"\n{today}: Authentication Error {device_name} {device_ip}")
        error_log_file.close()

    except Exception as e:
        print(f"\n{today}: something went wrong accessing {device_name} {device_ip} \n {e}")
        error_log_file = open(logging_file, "a")
        error_log_file.write(f"\n{today}: something went wrong accessing {device_name} {device_ip} \n {e}")
        error_log_file.close()
