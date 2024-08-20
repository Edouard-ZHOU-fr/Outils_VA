# Script for VRTK Calibration : compute averae difference between Track and Heading.
import re
import math
import csv
import time
import numpy as np
import geopy.distance
import pyproj
from geographiclib.geodesic import Geodesic
import matplotlib.pyplot as pl
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
startTime = time.time()



# SCRIPT PARAMETERS
inputFileName = "calibration_heading_5.txt"
baseline = 2.26 # Baseline to compute antenna offset (m)
speedThreshold = 40 # (km/h) Recommended to consider track values only above 40 km/h
debugOption = True # Activate debug information and graphs

# Read input text file
textFile = open(inputFileName, "r")
rawLines = textFile.readlines()
textFile.close()


# Initialize a few things
startTime = time.time()
newGGA = 0
newHDT = 0
j=0
points = np.zeros(shape=(len(rawLines),4)) # columns are : timestamp / latitude / longitude / heading


# For each new GGA and Ping line, add a line in the output array
for i in range(len(rawLines)):
    line = re.split(' |,',rawLines[i])

    if line[0] == '$GPGGA':
        # Line contains GGA
        timestamp = float(line[1])
        latDeci = float(line[2])
        latitude = math.floor(latDeci/100) + (latDeci/100 - math.floor(latDeci/100))/0.6
        lonDeci = float(line[4])
        longitude = math.floor(lonDeci/100) + (lonDeci/100 - math.floor(lonDeci/100))/0.6
        newGGA = 1
    elif line[0] == '$GPHDT':
        # Line contains HDT
        heading = float(line[1])
        newHDT = 1

    if newGGA == 1 and newHDT == 1:
        points[j,0] = float(timestamp)
        points[j,1] = float(latitude)
        points[j,2] = float(longitude)
        points[j,3] = float(heading)
        newGGA = 0
        newHDT = 0
        j=j+1

for i in range(len(points)-1,1,-1):
    if points[i,0] == 0:
        points = np.delete(points, i, 0)

# Compute track between all coordinates if speed is above speedThreshold
allHeading = []
allTrack = []
geodesic = pyproj.Geod(ellps='WGS84')

for i in range(1,len(points)):
    distance = geopy.distance.geodesic((points[i,1],points[i,2]), (points[i-1,1],points[i-1,2])).m
    if distance != 0: 
        speed = geopy.distance.geodesic((points[i,1],points[i,2]), (points[i-1,1],points[i-1,2])).m * 3.6 / (points[i,0]-points[i-1,0])
    else:
        speed = 0
    
    if speed >= speedThreshold:
        track = Geodesic.WGS84.Inverse(points[i-1,1], points[i-1,2], points[i,1], points[i,2])['azi1']
        if track < 0: track = track + 360
        allTrack.append(track)
        allHeading.append(points[i,3])
        if debugOption == True:
            print("Heading : %.2f / Track : %.3f " % (points[i,3], track))
        

print("Nombre de valeurs prises en compte pour le calcul : %s " % len(allHeading))

meanHeading = sum(allHeading) / len(allHeading)
print("Heading moyen : %.2f " % meanHeading)

meanTrack = sum(allTrack) / len(allTrack)
print("Track moyen : %.2f " % meanTrack)

ecart = meanHeading - meanTrack
print("Baseline : %.3f m." % baseline)
print("Ecart moyen heading - track = %.2f degrés." % ecart)

offsetFrontAntenna = 100 * math.tan(abs(ecart)*math.pi/180) * baseline # (cm) Offset to correct heading calibration.

if ecart > 0:
    print("L'antenne avant doit être décalée vers la droite de : %.1f cm." % offsetFrontAntenna)
else:
    print("L'antenne avant doit être décalée vers la gauche de : %.1f cm." % offsetFrontAntenna)


if debugOption == True:
    pl.figure()
    pl.plot(allHeading,color='blue',label='Heading')
    pl.plot(allTrack,color='red',label='Track')
    pl.legend(loc='upper right')


    # Plot results with Cartopy
    # pl.figure()
    # request = cimgt.OSM()
    # fig = pl.axes(projection=request.crs)
    # fig.add_image(request, 15) # Set zoom level
    # scatter = pl.scatter(points[:,2], points[:,1], s=5, alpha = 1, color='blue', transform=ccrs.PlateCarree())
    
    pl.show()



# Display total computing time
print("--- %.3f seconds ---" % (time.time() - startTime))