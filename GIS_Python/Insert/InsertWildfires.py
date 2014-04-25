# InsertWildfires.py
# Purpose: The purpose of this program is a take the feature in WildlandFires.mdb
#         the create the points for the feature based on a text file passed. Also
#         add and attribute of confidence. 
# Author: Jon Nordling
# Date: 02/06/13

import arcpy
import os

try:
    # Thes are user defined inputs for the workspace aswell as the wildfire text file
    arcpy.env.workspace=raw_input('Specify WildlandFires.mdb with full path: ')
    file_name = raw_input('Specify the wildfire text file with full path: ')
    
    # This opens the file 
    f = open(file_name, 'r')
    # read all the lines in the file
    lstFires = f.readlines()

    # creating a count
    count = 0
    # creating a cursor on the feature
    cur = arcpy.InsertCursor("FireIncidents")

    # This is loop that goes through each of the lines in the file
    # Determines if it is the header, if it is not then moves to 
    # creating points in the feature and defining the confidence level
    # as on of it attributes
    for fire in lstFires:
        if 'Latitude' in fire:
            continue
        else:
            # Defining the variable in the line 
            values = fire.split(",")
            lat = float(values[0])
            lng = float(values[1])
            con = int(values[2])

            # Creating the point object
            pnt = arcpy.CreateObject("Point")
            pnt.X = lng
            pnt.Y = lat

            # Geting the row and incerting the attributes to the 
            feat = cur.newRow()
            feat.shape = pnt
            feat.setValue("CONFIDENCEVALUE",con)
            cur.insertRow(feat)
            print 'Record number ' + str(count) + " written to feature class "
            # Increasing the counter 
            count = count +1
    # Deleting the cursor from the memory
    del cur
    del feat
    # Close the file that is open
    f.close()
    # Print out to the user the total number of inserted
    print 'Insert Complete! Total ' + str(count) + " points are inserted! "
        
    
except Exception, e:
    # Catching Errors it program fails
    print e
    print arcpy.GetMessages()
