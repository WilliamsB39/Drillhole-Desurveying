#Average Angle Method

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

Azimuth = (180/pi) * ((Az1[L] + Az2[L]) / 2)
Plunge = (180/pi) * ((P1[L] + P2[L]) / 2)

Depth <- DepthDiffs*sin((P1 + P2)/2)
North <- DepthDiffs*cos((P1 + P2)/2)*cos((Az1 + Az2)/2)
East  <- DepthDiffs*cos((P1 + P2)/2)*sin((Az1 + Az2)/2)

SumDepth <- round(c(0, cumsum(Depth)), digits = 2)
SumNorth <- round(c(0, cumsum(North)), digits = 2)
SumEast <- round(c(0, cumsum(East)), digits = 2)

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