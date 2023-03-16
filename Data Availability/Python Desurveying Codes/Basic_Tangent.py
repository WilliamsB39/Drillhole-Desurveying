# -*- coding: utf-8 -*-
"""
Created: 26 May 2020

@author: Benjamin Williams
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Survey = np.genfromtxt('#File#.csv', delimiter = ',', skip_header=2, usecols=(0,1,2))

Dn =  #Input distance of interest here

Depth = Survey[:, 0] #Call Depth data
AzimuthDegrees = Survey[:, 1] #Call Azimuth data
PlungeDegrees  = Survey[:, 2] #Call Plunge data

DepthDn = np.append(Depth[Depth < Dn], Dn)    #This step takes only Depth values < Dn value, adding Dn to the list

DepthDiffs = np.diff(DepthDn) #Distance along drillhole between survey points
AzimuthRadians = np.radians(AzimuthDegrees) #Convert degrees to radians
PlungeRadians = np.radians(PlungeDegrees) #Convert degrees to radians

ListLength = (np.prod(Depth.shape) - np.prod(DepthDiffs.shape))*-1   #Difference between the total length intervals in all drillhole and distances up to point of interest

Az1 = AzimuthRadians[:ListLength] #Azimuth at first survey in each survey point pair - not used in basic tangent method
P1  = PlungeRadians[:ListLength] #Plunge at first survey in each survey point pair - not used in basic tangent method

    #If statement for if list = 0, i.e. Dn > penultimate survey point depth
if ListLength + 1 < 0:
    ListLength = ListLength + 1
else:
    ListLength = None

Az2 = AzimuthRadians[1:ListLength] #Uses only the data from the second survey in each survey point pair
P2  = PlungeRadians[1:ListLength] #Uses only the data from the second survey in each survey point pair

Depth = DepthDiffs*np.sin(P2) #Difference in depths between survey points
North = DepthDiffs*np.cos(P2)*np.cos(Az2) #Difference in northing between survey points
East  = DepthDiffs*np.cos(P2)*np.sin(Az2) #Difference in easting between survey points

SumDepth = np.cumsum(Depth) #Sums the depths
SumNorth = np.cumsum(North) #Sums the northings
SumEast  = np.cumsum(East) #Sums the eastings

SumDepth = np.insert(SumDepth, 0, 0.0) #Adds the drillhole collar depth
SumNorth = np.insert(SumNorth, 0, 0.0) #Adds the drillhole collar northing
SumEast  = np.insert(SumEast,  0, 0.0) #Adds the drillhole collar easting

print('Depth at point:', SumDepth[-1])
print('North at point:', SumNorth[-1])
print('East at point:', SumEast[-1])
print('Azimuth at Dn Depth:', np.degrees(Az2)[-1])
print('Plunge at Dn Depth:', np.degrees(P2)[-1])

ax = plt.axes(projection='3d')

ax.scatter3D(SumEast, SumNorth, SumDepth, color='blue')
ax.plot3D(SumEast, SumNorth, SumDepth, 'blue')

#ax.set_xlim(#, #)
#ax.set_ylim(#, #)
#ax.set_zlim(#, #)
ax.set_xlabel('East (m)')
ax.set_ylabel('North (m)')
ax.set_zlabel('Depth (m)')

ax.set_title('Basic Tangent Method')

plt.show()