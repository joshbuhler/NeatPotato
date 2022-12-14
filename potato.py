import bpy
import os
import sys
from xml.dom.minidom import parse
from xml.dom.minidom import Node
from os import listdir
from os.path import isfile, join



class NeatPotato:

    __slots__ = ('filePath')

    def __init__(self, blenderContext, svgFilepath):
        print ("What is it with you and potatoes?")

        print("🥔 Loading SVG: " + svgFilepath)

        self.filePath = svgFilepath

    def parse(self):
        print("🍟 Parsing: " + self.filePath)
        domData = parse(self.filePath)

        parentGNode = domData.documentElement.getElementsByTagName("g")[0]
        weekGNodes = parentGNode.getElementsByTagName("g")

        currentX = 0.0
        currentY = 0.0

        # All units are in meters
        borderSize = 0.0
        spacing = 1.0
        towerSize = 2.0
        minHeight = 1.0
        baseHeight = 2.0

        currentX += borderSize
        currentY += borderSize

        maxCurrentY = 0.0

        applyBevel = True

        currentWeek = 0
        totalWeeks = len(weekGNodes)

        sys.stdout.write("[%s]" % (" " * totalWeeks))
        sys.stdout.flush()
        sys.stdout.write("\b" * (totalWeeks+1)) # return to start of line, after '['
        
        for week in weekGNodes:
            dayRects = week.getElementsByTagName("rect")

            sys.stdout.write("-")
            sys.stdout.flush()
            
            # reset for a new week
            currentY = borderSize
            
            for day in dayRects:
                date = day.getAttribute("data-date")
                dataLevel = (float(day.getAttribute("data-level")) * 1.5) + minHeight

                # print("Week: %2d" % currentWeek + "/%2d" % totalWeeks + " Date: " + date + " Level: %2d" % (dataLevel) + " x|y: %2d|%2d" % (currentX, currentY))
                
                bpy.ops.mesh.primitive_cube_add(size=towerSize,
                    enter_editmode=False,
                    align='WORLD',
                    location=(currentX + (towerSize / 2), currentY + (towerSize / 2), 0),
                    scale=(1, 1, 1))
                bpy.context.object.dimensions = (2, 2, dataLevel)

                #bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
                        
                if applyBevel:
                    bpy.ops.object.modifier_add(type="BEVEL")
                    bpy.context.object.modifiers["Bevel"].segments = 10
                    bpy.context.object.modifiers["Bevel"].width = 0.2

                currentY += towerSize
                currentY += spacing
                
                if currentY >= maxCurrentY:
                    maxCurrentY = currentY

            currentX += towerSize
            currentX += spacing
            currentWeek += 1

        sys.stdout.write("]\n") # this ends the progress bar
            
        # Put a base on this
        currentX -= spacing
        maxCurrentY -= spacing
        bpy.ops.mesh.primitive_cube_add(size=1.0,
            enter_editmode=False,
            align='WORLD',
            location=(currentX / 2, maxCurrentY / 2, 0),
            scale=(currentX, maxCurrentY, baseHeight))

        if applyBevel:
            bpy.ops.object.modifier_add(type="BEVEL")
            bpy.context.object.modifiers["Bevel"].segments = 10
            bpy.context.object.modifiers["Bevel"].width = 0.2

        # Select everything
        bpy.ops.object.select_all(action="SELECT")

        bpy.ops.object.align_tools(loc_z=True, ref1='0') # towers on TOP of base
        #bpy.ops.object.align_tools(loc_z=True, ref1='0', ref2='0') # towers at BOTTOM of base

            
            
            

        print ("🥔 I just think they're neat!")