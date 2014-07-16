# Daniel Hulsey
# Chapter 6
# Challenge 1
# Write a script that reads all the feature classes in a workspace and prints
# the name of each feature class and the geometry type of that feature
# class in the following format:
#   streams is a point feature class

import arcpy
from arcpy import env
env.workspace = "G:/Python/Python/Data/Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    properties = arcpy.Describe(fc)
    name = properties.name
    kind = properties.dataType
    print "{} is a {} feature class.".format(name, kind)

# Challenge 2
# Write a script that reads all the feature classes in a personal or file
# geodatabase and copies only the polygon feature classes to a new file
# geodatabase. You can assume there are no feature datasets in the existing
# data, and the feature classes can keep the same name.

import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "G:/Python/Python/Data/Exercise06"
arcpy.CreateFileGDB_management("G:/Python/Python/Data/Exercise06/Results", "challenge.gdb")
fclist = arcpy.ListFeatureClasses("", "poly")
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "G:/Python/Python/Data/Exercise06/Results/challenge.gdb/" + fcdesc.basename) 

