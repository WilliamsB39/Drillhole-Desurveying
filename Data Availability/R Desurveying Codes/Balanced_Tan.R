#Balanced Tangent Method

library(plot3D)
library(plot3Drgl)

Survey <- read.csv("#File#.csv", skip = 1, header = TRUE,)[,1:3] #Import drillhole survey data file

Dn <- #Input distance of interest here

Depth <- Survey[,"Depth..m."] #Call Depth data
AzimuthDegrees <- Survey[,"Az.Deg"] #Call Azimuth data
PlungeDegrees <- Survey[,"P.Deg"] #Call Plunge data

DepthDn <- append(Depth[Depth < Dn], Dn) #This step takes only Depth values < Dn value, adding Dn to the list

DepthDiffs <- diff(DepthDn)  #Distance along drillhole between survey points
AzimuthRadians <- (AzimuthDegrees * pi/180)  #Convert Azimuth degrees to radians
PlungeRadians <- (PlungeDegrees * pi/180)  #Convert Plunge degrees to radians

    #Difference between the total length intervals in all drillhole and distances up to Dn point of interest
ListLength <- (length(Depth) - length(DepthDiffs))
L <- length(Depth) - ListLength

D1 <- Depth[1:L] #Depth at first survey in each survey point pair
Az1 <- AzimuthRadians[1:L] #Azimuth at first survey in each survey point pair
P1 <- PlungeRadians[1:L] #Plunge at first survey in each survey point pair

D2 <- Depth[2:(L+1)] #Depth at second survey in each survey point pair
Az2 <- AzimuthRadians[2:(L+1)] #Azimuth at second survey in each survey point pair
P2 <- PlungeRadians[2:(L+1)] #Plunge at second survey in each survey point pair

MD <- (D2-D1) #Downhole distances between successive survey points

    #Calculate Azimuth and Plunge for Dn location
if (Dn <= (D1[L] + (MD[L]/2))) {
    Azimuth = (180/pi) * Az1[L]
    Plunge = (180/pi) * P1[L]
} else {
    Azimuth = (180/pi) * Az2[L]
    Plunge = (180/pi) * P2[L]
}

    #Calculate relative depths, northings and eastings at Dn location
if (Dn <= D1[L] + (MD[L]/2)){
    Dp = (Dn - D1[L]) * (sin(P1[L]))
    Np = (Dn - D1[L]) * (cos(P1[L])) * (cos(Az1[L]))
    Ep = (Dn - D1[L]) * (cos(P1[L])) * (sin(Az1[L]))
} else {
    Dp = ((Dn - D1[L] - (MD[L]/2)) * (sin(P2[L]))) + ((MD[L]/2) * sin(P1[L]))
    Np = ((Dn - D1[L] - (MD[L]/2)) * cos(P2[L]) * cos(Az2[L])) + ((MD[L]/2) * cos(P1[L]) * cos(Az1[L]))
    Ep = ((Dn - D1[L] - (MD[L]/2)) * cos(P2[L]) * sin(Az2[L])) + ((MD[L]/2) * cos(P1[L]) * sin(Az1[L]))
}

Depth <- (MD/2)*(sin(P1) + sin(P2)) #Difference in depths between survey points
North <- (MD/2)*((cos(P1)*cos(Az1)) + (cos(P2)*cos(Az2))) #Difference in northing between survey points
East  <- (MD/2)*((cos(P1)*sin(Az1)) + (cos(P2)*sin(Az2))) #Difference in easting between survey points

SumDepth <- round(cumsum(c(0, Depth[1:L-1], Dp)), digits = 2) #Sums the depths and adds collar coordinate
SumNorth <- round(cumsum(c(0, North[1:L-1], Np)), digits = 2) #Sums the northings and adds collar coordinate
SumEast <- round(cumsum(c(0, East[1:L-1], Ep)), digits = 2) #Sums the eastings and adds collar coordinate

    #Plot 3D graph
scatter3Drgl(SumEast,
             SumNorth,
             SumDepth,
             colvar = NULL,
             type = "o",
             #xlim = c(#,#),
             #ylim = c(#,#),
             #zlim = c(#,#),
             xlab = "East (m)",
             ylab = "North (m)",
             zlab = "Depth (m)",
             ticktype = "detailed")

scatter3D(SumEast,
          SumNorth,
          SumDepth,
          colvar = NULL,
          type = "o",
          #xlim = c(#,#),
          #ylim = c(#,#),
          #zlim = c(#,#),
          xlab = "East (m)",
          ylab = "North (m)",
          zlab = "Depth (m)",
          phi = 30,
          theta = 30,
          ticktype = "detailed",
          nticks = 14,
          bty = "g")

    #Show on graph the East, North, Depth, Azimuth and Plunge at Dn location
legend("bottomleft",
       inset = c(0,0),
       legend = c(parse(text = sprintf('paste(East~(m),\': %s\')', SumEast[L+1])),
                  parse(text = sprintf('paste(North~(m),\': %s\')', SumNorth[L+1])),
                  parse(text = sprintf('paste(Depth~(m),\': %s\')', SumDepth[L+1])),
                  parse(text = sprintf('paste(Azimuth~(degree),\': %s\')', Azimuth)),
                  parse(text = sprintf('paste(Plunge~(degree),\': %s\')', Plunge))),
       bty = "n",
       cex = 0.6)