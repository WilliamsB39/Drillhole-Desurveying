#Basic Tangent Method

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
L <- length(AzimuthRadians) - ListLength

Az1 <- AzimuthRadians[1:L]
P1 <- PlungeRadians[1:L]

Az2 <- AzimuthRadians[2:(L+1)]
P2 <- PlungeRadians[2:(L+1)]

Depth <- DepthDiffs * sin(P2)
North <- DepthDiffs * cos(P2) * cos(Az2)
East <- DepthDiffs * cos(P2) * sin(Az2)

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
                  parse(text = sprintf('paste(Azimuth~(~degree~C),\': %s\')', (180/pi)*Az2[L])),
                  parse(text = sprintf('paste(Plunge~(~degree~C),\': %s\')', (180/pi)*P2[L]))),
       bty = "n",
       cex = 0.6)