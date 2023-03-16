# -*- coding: utf-8 -*-
"""
Created: 26 May 2020

@author: Benjamin Williams
"""

import numpy as np
import matplotlib.pyplot as plt

Survey = np.genfromtxt('#File#.csv', delimiter = ',', skip_header=2, usecols=(0,1,2))

Dn = #

Depth = Survey[:, 0]
AzimuthDegrees = Survey[:, 1]
PlungeDegrees  = Survey[:, 2]

DepthDn = np.append(Depth[Depth < Dn], Dn)

DepthDiffs = np.diff(DepthDn)
AzimuthRadians = np.radians(AzimuthDegrees)
PlungeRadians = np.radians(PlungeDegrees)

ListLength = (len(Depth) - len(DepthDiffs)) * -1

D1   = Depth[:ListLength]
Az1  = AzimuthRadians[:ListLength]
P1   = PlungeRadians[:ListLength]
Az1D = AzimuthDegrees[:ListLength]
P1D  = PlungeDegrees[:ListLength]

if ListLength + 1 < 0:
    ListLength = ListLength + 1
else:
    ListLength = None

D2   = Depth[1:ListLength]
Az2  = AzimuthRadians[1:ListLength]
P2   = PlungeRadians[1:ListLength]
Az2D = AzimuthDegrees[1:ListLength]
P2D  = PlungeDegrees[1:ListLength]

MD = (D2 - D1)

if Dn <= (D1[-1] + (MD[-1]/2)):
    Azimuth = Az1D[-1]
    Plunge = P1D[-1]
else:
    Azimuth = Az2D[-1]
    Plunge = P2D[-1]

if Dn <= D1[-1] + (MD[-1] / 2):
    Dp = (Dn - D1[-1]) * (np.sin(P1[-1]))
    Np = (Dn - D1[-1]) * (np.cos(P1[-1]) * np.cos(Az1[-1]))
    Ep = (Dn - D1[-1]) * (np.cos(P1[-1]) * np.sin(Az1[-1]))
else:
    Dp = ((Dn - D1[-1] - (MD[-1]/2)) * np.sin(P2[-1])) + (MD[-1]/2) * np.sin(P1[-1])
    Np = ((Dn - D1[-1] - (MD[-1]/2)) * np.cos(P2[-1]) * np.cos(Az2[-1])) + ((MD[-1]/2) * np.cos(P1[-1]) * np.cos(Az1[-1]))
    Ep = ((Dn - D1[-1] - (MD[-1]/2)) * np.cos(P2[-1]) * np.sin(Az2[-1])) + ((MD[-1]/2) * np.cos(P1[-1]) * np.sin(Az1[-1]))
    
Depth = (MD/2)*(np.sin(P1) + np.sin(P2))
North = (MD/2)*((np.cos(P1)*np.cos(Az1)) + (np.cos(P2)*np.cos(Az2)))
East  = (MD/2)*((np.cos(P1)*np.sin(Az1)) + (np.cos(P2)*np.sin(Az2)))

SumDepth = np.cumsum(np.append(Depth[:-1], Dp))
SumNorth = np.cumsum(np.append(North[:-1], Np)) 
SumEast  = np.cumsum(np.append(East[:-1],  Ep))

SumDepth = np.insert(SumDepth, 0, 0.0)
SumNorth = np.insert(SumNorth, 0, 0.0)
SumEast  = np.insert(SumEast,  0, 0.0)

print('Depth at point:', SumDepth[-1])
print('North at point:', SumNorth[-1])
print('East at point:',  SumEast[-1])
print('Azimuth at Dn Depth:', Azimuth)
print('Plunge at Dn Depth:', Plunge)

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