import os
from math import floor
from stack import Stack
from credentials import *

toBeDistributedStack = Stack()

for folder,subFolder,file in os.walk(TO_BE_DISTIBUTED_FOLDER):
    for i in file:
        fileInfo = {
            "file":i,
            "folder":folder
        }
        toBeDistributedStack.push(fileInfo);
    break

sizeOfToBeDistributedStack = toBeDistributedStack.size()


otherAudioFiles = []
for folder,subFolder,file in os.walk(NON_DISTIRUBTED_FOLDER):
    path = NON_DISTIRUBTED_FOLDER+TO_BE_DISTIBUTED_FOLDER_SUB
    if path == folder:
        continue
    for i in file:
        fileInfo = {"file":i,"folder":folder}
        otherAudioFiles.append(fileInfo);
        

insertIdx = floor(len(otherAudioFiles) / sizeOfToBeDistributedStack)


distibutedList = []


for idx,file in enumerate(otherAudioFiles):
    if not (idx % insertIdx):
        if not toBeDistributedStack.isEmpty():
            distibutedList.append(toBeDistributedStack.pop())
    distibutedList.append(file)
    pass


def rename(old,new):
    os.rename(old,new)

for idx,file in enumerate(distibutedList):
    print(file)
    old = file["folder"] + "\\" + file["file"] 
    new = file["folder"] + "\\" + str(idx) + "-" + file["file"]
    
    break
    # rename the curent file
    # move the file to the desired location