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

Az1  = AzimuthRadians[:ListLength]
P1   = PlungeRadians[:ListLength]
Az1D = AzimuthDegrees[:ListLength]
P1D  = PlungeDegrees[:ListLength]

if ListLength + 1 < 0:
    ListLength = ListLength + 1
else:
    ListLength = None

Az2  = AzimuthRadians[1:ListLength]
P2   = PlungeRadians[1:ListLength]
Az2D = AzimuthDegrees[1:ListLength]
P2D  = PlungeDegrees[1:ListLength]

Azimuth = (Az1D + Az2D) / 2
Plunge = (P1D + P2D) / 2

Depth = DepthDiffs*np.sin((P1 + P2)/2)
North = DepthDiffs*np.cos((P1 + P2)/2)*np.cos((Az1 + Az2)/2)
East  = DepthDiffs*np.cos((P1 + P2)/2)*np.sin((Az1 + Az2)/2)

SumDepth = np.cumsum(Depth)
SumNorth = np.cumsum(North)
SumEast  = np.cumsum(East)

SumDepth = np.insert(SumDepth, 0, 0.0)
SumNorth = np.insert(SumNorth, 0, 0.0)
SumEast  = np.insert(SumEast,  0, 0.0)

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