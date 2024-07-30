# Convert data from tf topic to a CSV file containing a trajectory for VectorMapBuilder.
# Input : text file from topic "tf"
# Output : CSV file that can be loaded into VectorMapBuilder

# Format : X,Y,Z,yaw
import re
import math
import csv
import time


# SCRIPT PARAMETERS
inputFileName = "1.txt"
filterRate = 20 # If topic frequency is 20Hz, set parameter to '20' to get 1 point every 20 tf value (meaning 1 point per second as output trajectory)


# Initialize a few things
outputFileName = inputFileName.replace('.txt', '.csv')
startTime = time.time()
output=[]
outputFilter=[]
newX = 0
newY = 0
newZ = 0
Z = 0

# Read input text file
textFile = open(inputFileName, "r")
rawLines = textFile.readlines()
textFile.close()

# Create a header in the output array (x,y,z,yaw)
output.append(['x', 'y', 'z', 'yaw'])

for i in rawLines:
    line = re.split(' |,',i)
    line = [item for item in line if item != ""]
    line = [item.rstrip('\n') for item in line]

    if len(line) >= 2:
        if line[0] == 'x:' and float(line[1]) >=10 :
            X = float(line[1])
            newX = 1

        elif line[0] == 'y:' and float(line[1]) >=10 :
            Y = float(line[1])
            newY = 1

        elif line[0] == 'z:' and float(line[1]) >=10 :
            Z = float(line[1])
            newZ = 1

    
    if newX == 1 and newY ==1 and newZ ==1:
        output.append([X, Y, Z, 0])
        newX = 0
        newY = 0
        newZ = 0

j=0
for i in output:
    j=j+1
    if j % filterRate == 1:  # Write only every n line
        outputFilter.append(i)




# Write results in the output file
with open(outputFileName, 'w', newline='') as f:
    csv.writer(f, delimiter=',').writerows(outputFilter)



# Display total computing time
print("--- %.3f seconds ---" % (time.time() - startTime))
