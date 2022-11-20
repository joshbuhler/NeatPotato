import bpy
import os
import sys
from xml.dom.minidom import parse
from xml.dom.minidom import Node
from os import listdir
from os.path import isfile, join


print ("What is it with you and potatoes?")

filePath = "/Users/josh/Projects/stunning-potato/testSvg/graph1.svg"
#filePath = "testSvg/graph1.svg"
domData = parse(filePath)

parentGNode = domData.documentElement.getElementsByTagName("g")[0]

weekGNodes = parentGNode.getElementsByTagName("g")


currentX = 0.0
currentY = 0.0

# All units are in meters
borderSize = 0.0
spacing = 1.0
towerSize = 2.0
minHeight = 1.0

currentX += borderSize
currentY += borderSize

for week in weekGNodes:
    dayRects = week.getElementsByTagName("rect")
    for day in dayRects:
        date = day.getAttribute("data-date")
        dataLevel = float(day.getAttribute("data-level")) + minHeight

        print("Date: " + date + " Level: %2d" % (dataLevel) + " x|y: %2d|%2d" % (currentX, currentY))
        
        bpy.ops.mesh.primitive_cube_add(size=towerSize,
            enter_editmode=False,
            align='WORLD',
            location=(currentX, currentY, 0),
            scale=(1, 1, dataLevel))

        currentY += towerSize
        currentY += spacing

    # week ended - reset
    currentY = borderSize

    currentX += towerSize
    currentX += spacing
    