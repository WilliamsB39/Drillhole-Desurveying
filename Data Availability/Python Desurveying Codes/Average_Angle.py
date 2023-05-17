# -*- coding: utf-8 -*-
"""
Created: 26 May 2020

@author: Benjamin Williams
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Survey = np.genfromtxt('#File#.csv', delimiter = ',', skip_header=2, usecols=(0,1,2)) #Import drillhole survey data file

Dn = #Input distance of interest here

Depth = Survey[:, 0] #Call Depth data
AzimuthDegrees = Survey[:, 1] #Call Azimuth data
PlungeDegrees  = Survey[:, 2] #Call Plunge data

DepthDn = np.append(Depth[Depth < Dn], Dn)    #This step takes only Depth values < Dn value, adding Dn to the list

DepthDiffs = np.diff(DepthDn)  #Distance along drillhole between survey points
AzimuthRadians = np.radians(AzimuthDegrees) #Convert Azimuth degrees to radians
PlungeRadians = np.radians(PlungeDegrees) #Convert Plunge degrees to radians

ListLength = (len(Depth) - len(DepthDiffs)) * -1  #Difference between the total length intervals in all drillhole and distances up to Dn point of interest

Az1  = AzimuthRadians[:ListLength] #Azimuth at first survey in each survey point pair - radians
P1   = PlungeRadians[:ListLength] #Plunge at first survey in each survey point pair - radians
Az1D = AzimuthDegrees[:ListLength] #Azimuth at first survey in each survey point pair - degrees
P1D  = PlungeDegrees[:ListLength] #Plunge at first survey in each survey point pair - degrees

    #If statement for if list = 0, i.e. Dn > penultimate survey point depth
if ListLength + 1 < 0:
    ListLength = ListLength + 1
else:
    ListLength = None

Az2  = AzimuthRadians[1:ListLength] #Azimuth at second survey in each survey point pair - radians
P2   = PlungeRadians[1:ListLength] #Plunge at second survey in each survey point pair - radians
Az2D = AzimuthDegrees[1:ListLength] #Azimuth at second survey in each survey point pair - degrees
P2D  = PlungeDegrees[1:ListLength] #Plunge at second survey in each survey point pair - degrees

    #Calculate Azimuth and Plunge for Dn location
Azimuth = (Az1D + Az2D) / 2
Plunge = (P1D + P2D) / 2

    #Calculate and sum all depths, northings and eastings cumulatively down the drillhole
Depth = DepthDiffs*np.sin((P1 + P2)/2)
North = DepthDiffs*np.cos((P1 + P2)/2)*np.cos((Az1 + Az2)/2)
East  = DepthDiffs*np.cos((P1 + P2)/2)*np.sin((Az1 + Az2)/2)

SumDepth = np.cumsum(Depth)
SumNorth = np.cumsum(North)
SumEast  = np.cumsum(East)

SumDepth = np.insert(SumDepth, 0, 0.0)
SumNorth = np.insert(SumNorth, 0, 0.0)
SumEast  = np.insert(SumEast,  0, 0.0)

    #Plot 3D graph
print('Depth at point:', SumDepth[-1])
print('North at point:', SumNorth[-1])
print('East at point:', SumEast[-1])
print('Azimuth at Dn Depth:', Azimuth[-1])
print('Plunge at Dn Depth:', Plunge[-1])

ax = plt.axes(projection='3d')

ax.scatter3D(SumEast, SumNorth, SumDepth, color='blue')
ax.plot3D(SumEast, SumNorth, SumDepth, 'blue')

#ax.set_xlim(#, #)
#ax.set_ylim(#, #)
#ax.set_zlim(#, #)
ax.set_xlabel('East (m)')
ax.set_ylabel('North (m)')
ax.set_zlabel('Depth (m)')

ax.set_title('Average Angle Method')

plt.show()