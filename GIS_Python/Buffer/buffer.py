# Jon Nordling
# 01/14/10
# Purpose: The purpose of this program is to be used as a Arc GIS
#          toolbox script. The tool with create a buffer of the
#          AnnDiego Freeways of a specified distance from the user
#          The progam take 2 peramiter one being the output feature and
#          distance to buffer the roads. The output feature will will be
#          created in the workspace specified in the script.

import arcpy

# Step 1
#----------------------------------
# Set the current works space to the SanDiego.gdb 
arcpy.env.workspace = r"C:/Users/Jon/Dropbox/GEOG656/Lab5/all/SanDiego.gdb"

# Creates variables that will store user input values
# Will hold valuse for users for the Toolbox
output = arcpy.GetParameterAsText(0)    # holds the output directory
distance = arcpy.GetParameterAsText(1)  # holds the buffer distance

# Buffer the roads feature class by 2000 feet and create new feature called
arcpy.Buffer_analysis("Freeways", output, distance)

# This is a warning text that Arc will displat when the feature is created
arcpy.AddWarning("The Freeway"+output+"has be created")






