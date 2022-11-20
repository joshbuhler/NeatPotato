##import bpy
import os
import sys
from xml.dom.minidom import parse
from xml.dom.minidom import Node
from os import listdir
from os.path import isfile, join


print ("What is it with you and potatoes?")

filePath = "testSvg/graph1.svg"
domData = parse(filePath)

parentGNode = domData.documentElement.getElementsByTagName("g")[0]

weekGNodes = parentGNode.getElementsByTagName("g")


currentX = 0
currentY = 0

# All units are in meters
borderSize = 0
spacing = 1
towerSize = 2

currentX += borderSize
currentY += borderSize

for week in weekGNodes:
	dayRects = week.getElementsByTagName("rect")
	for day in dayRects:
		date = day.getAttribute("data-date")
		dataLevel = day.getAttribute("data-level")

		print("Date: " + date + " Level: " + dataLevel + " x|y: %2d|%2d" % (currentX, currentY))

		currentY += towerSize
		currentY += spacing

	# week ended - reset
	currentY = borderSize

	currentX += towerSize
	currentX += spacing