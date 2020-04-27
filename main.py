import os
from math import floor
from stack import Stack
from credentials import *

toBeDistributedStack = Stack()

for folder,subFolder,file in os.walk(TO_BE_DISTIBUTED_FOLDER):
    for i in file:
        toBeDistributedStack.push(file);
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
    print(idx,file)
    pass

# iterate over the audio files using emnumerators

        # check if the current index % (sum of audio file / sum of messages) equals to 0
            # check if the message stack is note empty
                # pop a message from the stack and add it to the distirbuted list
            # if it's 
                # break 
    
        # add the current audio file to the distributed list
    
# iterate over the distributed list usnig an enumerator
    # rename the curent file
    # move the file to the desired location