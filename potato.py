import bpy
import os
import sys
from xml.dom.minidom import parse
from xml.dom.minidom import Node
from os import listdir
from os.path import isfile, join




filePath = "/Users/josh/Projects/stunning-potato/testSvg/graph1.svg"

class StunningPotato:

    def __init__(self, blenderContext, svgFilepath):
        print ("What is it with you and potatoes?")

        print("🥔 Loading SVG: " + svgFilepath)





# #filePath = "testSvg/graph1.svg"
# domData = parse(filePath)

# parentGNode = domData.documentElement.getElementsByTagName("g")[0]

# weekGNodes = parentGNode.getElementsByTagName("g")


# currentX = 0.0
# currentY = 0.0

# # All units are in meters
# borderSize = 1.0
# spacing = 1.0
# towerSize = 2.0
# minHeight = 2.0

# currentX += borderSize
# currentY += borderSize

# maxCurrentY = 0.0

# applyBevel = False

# for week in weekGNodes:
#     dayRects = week.getElementsByTagName("rect")
    
#     # reset for a new week
#     currentY = borderSize
    
#     for day in dayRects:
#         date = day.getAttribute("data-date")
#         dataLevel = float(day.getAttribute("data-level")) + minHeight

#         print("Date: " + date + " Level: %2d" % (dataLevel) + " x|y: %2d|%2d" % (currentX, currentY))
        
#         bpy.ops.mesh.primitive_cube_add(size=towerSize,
#             enter_editmode=False,
#             align='WORLD',
#             location=(currentX + (towerSize / 2), currentY + (towerSize / 2), 0),
#             scale=(1, 1, dataLevel))
                
#         if applyBevel:
#             bpy.ops.object.modifier_add(type="BEVEL")
#             bpy.context.object.modifiers["Bevel"].segments = 10

#         currentY += towerSize
#         currentY += spacing
        
#         if currentY >= maxCurrentY:
#             maxCurrentY = currentY

#     currentX += towerSize
#     currentX += spacing
    
# # Put a base on this thing
# bpy.ops.mesh.primitive_cube_add(size=1.0,
#     enter_editmode=False,
#     align='WORLD',
#     location=(currentX / 2, maxCurrentY / 2, 0),
#     scale=(currentX, maxCurrentY, minHeight))
    
    
    

# print ("I just think they're neat!")