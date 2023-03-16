#Minimum Curvature Method

library(plot3D)
library(plot3Drgl)

Survey <- read.csv("#File#.csv", skip = 1, header = TRUE,)[,1:3]

Dn <- #

Depth <- Survey[,"Depth..m."]
AzimuthDegrees <- Survey[,"Az.Deg"]
PlungeDegrees <- Survey[,"P.Deg"]

DepthDn <- append(Depth[Depth < Dn], Dn)

DepthDiffs <- diff(DepthDn)
AzimuthRadians <- (AzimuthDegrees * pi/180)
PlungeRadians <- (PlungeDegrees * pi/180)

ListLength <- (length(Depth) - length(DepthDiffs))
L <- length(Depth) - ListLength

D1 <- Depth[1:L]
Az1 <- AzimuthRadians[1:L]
P1 <- PlungeRadians[1:L]

D2 <- Depth[2:(L+1)]
Az2 <- AzimuthRadians[2:(L+1)]
P2 <- PlungeRadians[2:(L+1)]

MD <- (D2-D1)

if (Dn <= D1[L] + (MD[L]/2)) {
  Azimuth = (180/pi) * Az1[L]
  Plunge = (180/pi) * P1[L]
} else {
  Azimuth = (180/pi) * Az2[L]
  Plunge = (180/pi) * P2[L]
}

ab <- ((sin(Az1) * cos(P1)) * (sin(Az2) * cos(P2))) + ((cos(Az1) * cos(P1)) * (cos(Az2) * cos(P2))) + (sin(P1) * sin(P2))
AB <- sqrt(((sin(Az1) * cos(P1))**2) + ((cos(Az1) * cos(P1))**2) + ((sin(P1))**2)) * sqrt(((sin(Az2) * cos(P2))**2) + ((cos(Az2) * cos(P2))**2) + ((sin(P2))**2))
Beta <- acos(ab/AB)
RF <- (tan(Beta/2)) / (Beta/2)

if (Dn <= D1[L] + (MD[L] / 2)) {
  Dp = (Dn - D1[L]) * (sin(P1[L])) * RF[L]
  Np = (Dn - D1[L]) * (cos(P1[L]) * cos(Az1[L])) * RF[L]
  Ep = (Dn - D1[L]) * (cos(P1[L]) * sin(Az1[L])) *RF[L]
} else {
  Dp = (((Dn - D1[L] - (MD[L]/2)) * sin(P2[L])) + (MD[L]/2) * sin(P1[L])) * RF[L]
  Np = (((Dn - D1[L] - (MD[L]/2)) * cos(P2[L]) * cos(Az2[L])) + ((MD[L]/2) * cos(P1[L]) * cos(Az1[L]))) * RF[L]
  Ep = (((Dn - D1[L] - (MD[L]/2)) * cos(P2[L]) * sin(Az2[L])) + ((MD[L]/2) * cos(P1[L]) * sin(Az1[L]))) * RF[L]
}

Depth <- (MD/2)*(sin(P1) + sin(P2))*RF
North <- (MD/2)*((cos(P1)*cos(Az1)) + (cos(P2)*cos(Az2)))*RF
East  <- (MD/2)*((cos(P1)*sin(Az1)) + (cos(P2)*sin(Az2)))*RF

SumDepth <- round(cumsum(c(0, Depth[1:L-1], Dp)), digits = 2)
SumNorth <- round(cumsum(c(0, North[1:L-1], Np)), digits = 2)
SumEast <- round(cumsum(c(0, East[1:L-1], Ep)), digits = 2)

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

legend("bottomleft",
       inset = c(0,0),
       legend = c(parse(text = sprintf('paste(East~(m),\': %s\')', SumEast[L+1])),
                  parse(text = sprintf('paste(North~(m),\': %s\')', SumNorth[L+1])),
                  parse(text = sprintf('paste(Depth~(m),\': %s\')', SumDepth[L+1])),
                  parse(text = sprintf('paste(Azimuth~(degree),\': %s\')', Azimuth)),
                  parse(text = sprintf('paste(Plunge~(degree),\': %s\')', Plunge))),
       bty = "n",
       cex = 0.6)