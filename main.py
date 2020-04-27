import os
from math import floor
from stack import Stack
from credentials import *

toBeDistributedStack = Stack()

for folder,subFolder,file in os.walk(TO_BE_DISTIBUTED_FOLDER):
    for i in file:
        fullFile = folder + "\\" + i 
        toBeDistributedStack.push(fullFile);
    break

sizeOfToBeDistributedStack = toBeDistributedStack.size()


otherAudioFiles = []
for folder,subFolder,file in os.walk(NON_DISTIRUBTED_FOLDER):
    path = NON_DISTIRUBTED_FOLDER+TO_BE_DISTIBUTED_FOLDER_SUB
    if path == folder:
        continue
    otherAudioFiles = otherAudioFiles + file



insertIdx = floor(len(otherAudioFiles) / sizeOfToBeDistributedStack)


distibutedList = []


for idx,file in enumerate(otherAudioFiles):
    if not (idx % insertIdx):
        if not toBeDistributedStack.isEmpty():
            distibutedList.append(toBeDistributedStack.pop())
    distibutedList.append(file)
    pass

    
for idx,file in enumerate(distibutedList):
    pass
    # rename the curent file
    # move the file to the desired location