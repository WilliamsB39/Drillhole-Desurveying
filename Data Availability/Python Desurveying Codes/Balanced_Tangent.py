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

DepthDiffs = np.diff(DepthDn) #Distance along drillhole between survey points
AzimuthRadians = np.radians(AzimuthDegrees) #Convert Azimuth degrees to radians
PlungeRadians = np.radians(PlungeDegrees) #Convert Plunge degrees to radians

ListLength = (len(Depth) - len(DepthDiffs)) * -1  #Difference between the total length intervals in all drillhole and distances up to Dn point of interest

D1   = Depth[:ListLength] #Depths at first survey in each survey point pair - metres
Az1  = AzimuthRadians[:ListLength] #Azimuth at first survey in each survey point pair - radians
P1   = PlungeRadians[:ListLength] #Plunge at first survey in each survey point pair - radians
Az1D = AzimuthDegrees[:ListLength] #Azimuth at first survey in each survey point pair - degrees
P1D  = PlungeDegrees[:ListLength] #Plunge at first survey in each survey point pair - degrees

    #If statement for if list = 0, i.e. Dn > penultimate survey point depth
if ListLength + 1 < 0:
    ListLength = ListLength + 1
else:
    ListLength = None

D2   = Depth[1:ListLength] #Depths at second survey in each survey point pair - metres
Az2  = AzimuthRadians[1:ListLength] #Azimuth at second survey in each survey point pair - radians
P2   = PlungeRadians[1:ListLength] #Plunge at second survey in each survey point pair - radians
Az2D = AzimuthDegrees[1:ListLength] #Azimuth at second survey in each survey point pair - degrees
P2D  = PlungeDegrees[1:ListLength] #Plunge at second survey in each survey point pair - degrees

MD = (D2 - D1) #Downhole distances between successive survey points

    #Calculate Azimuth and Plunge for Dn location
if Dn <= (D1[-1] + (MD[-1]/2)):
    Azimuth = Az1D[-1]
    Plunge = P1D[-1]
else:
    Azimuth = Az2D[-1]
    Plunge = P2D[-1]

    #Calculate relative depths, northings and eastings at Dn location
if Dn <= D1[-1] + (MD[-1] / 2):
    Dp = (Dn - D1[-1]) * (np.sin(P1[-1]))
    Np = (Dn - D1[-1]) * (np.cos(P1[-1]) * np.cos(Az1[-1]))
    Ep = (Dn - D1[-1]) * (np.cos(P1[-1]) * np.sin(Az1[-1]))
else:
    Dp = ((Dn - D1[-1] - (MD[-1]/2)) * np.sin(P2[-1])) + (MD[-1]/2) * np.sin(P1[-1])
    Np = ((Dn - D1[-1] - (MD[-1]/2)) * np.cos(P2[-1]) * np.cos(Az2[-1])) + ((MD[-1]/2) * np.cos(P1[-1]) * np.cos(Az1[-1]))
    Ep = ((Dn - D1[-1] - (MD[-1]/2)) * np.cos(P2[-1]) * np.sin(Az2[-1])) + ((MD[-1]/2) * np.cos(P1[-1]) * np.sin(Az1[-1]))
    
    #Sum all depths, northings and eastings cumulatively down the drillhole and append Dn data above
Depth = (MD/2)*(np.sin(P1) + np.sin(P2))
North = (MD/2)*((np.cos(P1)*np.cos(Az1)) + (np.cos(P2)*np.cos(Az2)))
East  = (MD/2)*((np.cos(P1)*np.sin(Az1)) + (np.cos(P2)*np.sin(Az2)))

SumDepth = np.cumsum(np.append(Depth[:-1], Dp))
SumNorth = np.cumsum(np.append(North[:-1], Np)) 
SumEast  = np.cumsum(np.append(East[:-1],  Ep))

SumDepth = np.insert(SumDepth, 0, 0.0)
SumNorth = np.insert(SumNorth, 0, 0.0)
SumEast  = np.insert(SumEast,  0, 0.0)

    #Print statements of Dn location
print('Depth at point:', SumDepth[-1])
print('North at point:', SumNorth[-1])
print('East at point:',  SumEast[-1])
print('Azimuth at Dn Depth:', Azimuth)
print('Plunge at Dn Depth:', Plunge)

    #Plot 3D graph
ax = plt.axes(projection='3d')

ax.scatter3D(SumEast, SumNorth, SumDepth, color='blue')
ax.plot3D(SumEast, SumNorth, SumDepth, 'blue')

#ax.set_xlim(#, #)
#ax.set_ylim(#, #)
#ax.set_zlim(#, #)
ax.set_xlabel('East (m)')
ax.set_ylabel('North (m)')
ax.set_zlabel('Depth (m)')

ax.set_title('Balanced Tangent Method')

plt.show()