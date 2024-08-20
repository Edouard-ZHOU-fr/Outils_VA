# Script for VRTK Calibration : compute distance between the 2 antennas.
import re
import math
import csv
import time
import numpy as np
import geopy.distance
startTime = time.time()



# SCRIPT PARAMETERS
inputFileName1 = "antenne_1.txt"
inputFileName2 = "antenne_2.txt"




# Read input text files
textFile1 = open(inputFileName1, "r")
rawLines1 = textFile1.readlines()
textFile1.close()

textFile2 = open(inputFileName2, "r")
rawLines2 = textFile2.readlines()
textFile2.close()


# Initialize a few things
startTime = time.time()
points1 = np.empty(shape=(len(rawLines1),2)) # columns are : latitude / longitude
points2 = np.empty(shape=(len(rawLines2),2)) # columns are : latitude / longitude


# For each new GGA and Ping line, add a line in the output array
for i in range(len(points1)):
    line = re.split(' |,',rawLines1[i])

    if line[0] == '$GPGGA':
        # Line contains GGA
        latDeci = float(line[2])
        latitude = math.floor(latDeci/100) + (latDeci/100 - math.floor(latDeci/100))/0.6
        lonDeci = float(line[4])
        longitude = math.floor(lonDeci/100) + (lonDeci/100 - math.floor(lonDeci/100))/0.6

        points1[i,0] = float(latitude)
        points1[i,1] = float(longitude)
        print(points1[i,:])

for i in range(len(points2)):
    line = re.split(' |,',rawLines2[i])

    if line[0] == '$GPGGA':
        # Line contains GGA
        latDeci = float(line[2])
        latitude = math.floor(latDeci/100) + (latDeci/100 - math.floor(latDeci/100))/0.6
        lonDeci = float(line[4])
        longitude = math.floor(lonDeci/100) + (lonDeci/100 - math.floor(lonDeci/100))/0.6

        points2[i,0] = float(latitude)
        points2[i,1] = float(longitude)
        print(points2[i,:])


# Compute average coordinates of the 2 antennas
latitude1 = sum(points1[:,0]) / len(points1[:,0])
longitude1 = sum(points1[:,1]) / len(points1[:,1])

latitude2 = sum(points2[:,0]) / len(points2[:,0])
longitude2 = sum(points2[:,1]) / len(points2[:,1])


# Compute distance between the average coordinates of the 2 antennas
baseline = geopy.distance.geodesic((latitude1,longitude1), (latitude2,longitude2)).m
print("\nBaseline : %.3f m.\n" % baseline)
print("Number of points used for each antenna : %s and %s.\n" % (len(points1), len(points2)))


# Display total computing time
print("--- %.3f seconds ---" % (time.time() - startTime))