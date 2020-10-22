import os
import glob


def isWritable(directory):
    try:
        os.makedirs(directory)
        filename = f"{directory}/temp_file.txt"
        testfile = open(filename, "w")
        testfile.write("Testing user privilege")
        testfile.close()
        os.remove(f'{filename}')
        return True
    except:
        return False


def isFileAvailable(directory, filename):
    try:
        file_name_list = []
        full_path = f'{directory}/{filename}*.txt'
        file_name_list.append(glob.glob(full_path)[0])
        return True
    except:
        return False



