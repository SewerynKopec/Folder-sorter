import os
import shutil
import time

source = R"C:\\Users\\$USERNAME\\Downloads"
destination = R"C:\\Users\\$USERNAME\\Documents"

destination += "\\SortedFiles"
if os.path.exists(destination) == False:
    os.mkdir(destination)

files = os.listdir(source)
for file in files:
    fileElements = file.split(".")
    if len(fileElements) > 1:
        extension = fileElements[len(fileElements)-1]
    else:
        extension = "NoExtension"
    extensionDir = destination + "\\" + extension

    if os.path.exists(extensionDir) == False:
        os.mkdir(extensionDir)
    shutil.move(source + "\\" + file, extensionDir)
