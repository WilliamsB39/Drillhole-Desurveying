# Drill-Hole-Desurveying

This repository relates to the manuscript: “The Impact of Anisotropy and Drillhole Length on the Existing Desurveying Methods: Examples from Mount Isa”
Authors: Williams, B.J. and Blenkinsop, T.G.
The codes presented here allow the user to plot drillhole pathways in Python or R using different desurveying methods (Basic Tangent, Balanced Tangent, Average Angle, Minimum Curvature) without sophisticated or commercial software. The code allows the azimuth, plunge and 3-dimensional coordinates to be calculated for any point along the drillhole. This enables the user to ascertain the orientation of drill core at any distance along the drillhole and locate points of interest, such as geological contacts, faults, or underground workings in 3-dimensional mine grid coordinates.

These codes are available in both Python (.py) and R (.R) languages and can be found in the respective folders ‘Python Desurveying Codes’ and ‘R Desurveying Codes’:
o	Basic Tangent Method
o	Balanced Tangent Method
o	Average Angle Method
o	Minimum Curvature Method

Modules/imports/libraries used in the code:
•	Python:
o	numpy
o	matplotlib.pyplot
o	mpl_toolkits.mplot3d.Axes3D
•	R
o	plot3D
o	plot3Drgl

How to run codes:
•	Data should be in the form of drillhole survey data in columns:
o	Column 1 (name: ‘Depth (m)’) – Depth intervals at survey points (metres)
o	Column 2 (name: ‘Az Deg’) – Azimuth measurement (degrees)
o	Column 3 (name: ‘P Deg’) – Plunge measurement (degrees)
•	Import drillhole survey data as .csv file by replacing ‘#File#.csv’ with file your path and file name.
•	State depth of interest as the Dn variable

Examples
Python:



R:
