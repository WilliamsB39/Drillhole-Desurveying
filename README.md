# Drill-Hole-Desurveying

This repository relates to the manuscript: “**The Impact of Anisotropy and Drillhole Length on the Existing Desurveying Methods: Examples from Mount Isa**”  
Authors: Williams, B.J. and Blenkinsop, T.G.  

The codes presented here allow the user to plot drillhole pathways in Python or R using different desurveying methods (Basic Tangent, Balanced Tangent, Average Angle, Minimum Curvature) without sophisticated or commercial software. The code allows the azimuth, plunge and 3-dimensional coordinates to be calculated for any point along the drillhole. This enables the user to ascertain the orientation of drill core at any distance along the drillhole and locate points of interest, such as geological contacts, faults, or underground workings in 3-dimensional mine grid coordinates.

These codes are available in both Python (.py) and R (.R) languages and can be found in the respective folders ‘Python Desurveying Codes’ and ‘R Desurveying Codes’:
  * Basic Tangent Method
  * Balanced Tangent Method  
  * Average Angle Method  
  * Minimum Curvature Method

Modules/imports/libraries used in the code:
  * Python:
    * numpy
    * matplotlib.pyplot
    * mpl_toolkits.mplot3d.Axes3D
  * R
    *	plot3D
    *	plot3Drgl

How to run codes:
  * Data should be in the form of drillhole survey data in columns:
    *	Column 1 (name: ‘Depth (m)’) – Depth intervals at survey points (metres)
    *	Column 2 (name: ‘Az Deg’) – Azimuth measurement (degrees)
    *	Column 3 (name: ‘P Deg’) – Plunge measurement (degrees)
  * Import drillhole survey data as .csv file by replacing ‘#File#.csv’ with file your path and file name.
  *	State depth of interest as the Dn variable

Example Python Output:  
![Average_Angle_Test_Survey_Python](https://github.com/WilliamsB39/Drillhole-Desurveying/assets/65358801/4d5cb867-8b58-4709-804f-5552882150a3)
Depth at point: 7.3228  
North at point: 21.8231  
East at point: 116.9278  
Azimuth at Dn Depth: 67.5  
Plunge at Dn Depth: 3.0  

  
Example R Output:  
![Average_Angle_Test_Survey_R](https://github.com/WilliamsB39/Drillhole-Desurveying/assets/65358801/ae7583ae-178e-4d89-90ef-6b6ea8c2a0f1)
