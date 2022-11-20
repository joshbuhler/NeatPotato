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

for week in weekGNodes:
	dayRects = week.getElementsByTagName("rect")
	for day in dayRects:
		date = day.getAttribute("data-date")
		dataLevel = day.getAttribute("data-level")

		print("Date: " + date + " Level: " + dataLevel)