import os
from stack import Stack
from credentials import *

toBeDistributedStack = Stack()

for folder,subFolder,file in os.walk(TO_BE_DISTIBUTED_FOLDER):
    for i in file:
        toBeDistributedStack.push(file);
    break

sizeOfToBeDistributedStack = toBeDistributedStack.size()





# store other audios files in a list

# get the total number of audio files

# get the total number of messages

# store the sum of audio file / sum of messages

# create the distributed list

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