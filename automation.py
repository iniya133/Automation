import os
import shutil
import time

def backupToExternalDrive():
    source = input("Enter the drive that is to be backed up: ")
    destination = "F:"

    source = source + '/'
    destination = destination + '/'

    list_of_files = os.listdir(source)

    seconds = time.time() - (30 * 24 * 60 * 60)


    if (seconds >= getAge(source)):

        with open(source, 'rb') as f:  
            shutil.copy(source, destination)


def getAge(path):

	ctime = os.stat(path).st_ctime

	return ctime


backupToExternalDrive()