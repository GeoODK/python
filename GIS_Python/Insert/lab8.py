# InsertWildfires.py
# Purpose:
# Author: Jon Nordling
# Date: 02/06/13

import arcpy
import os

try:
    arcpy.env.workspace='C:\Users\jnordling\Dropbox\GEOG656\Lab8\lab8_data\WildlandFires.mdb'
    file_name = './lab8_data/NorthAmericaWildfires_2007275.txt'
    
    f = open(file_name, 'r')
    lstFires = f.readlines()
    count = 1
    cur = arcpy.InsertCursor("FireIncidents")
    for fire in lstFires:
        if 'Latitude' in fire:
            continue
        else:
            values = fire.split(",")
            lat = float(values[0])
            lng = float(values[1])
            con = int(values[2])
            pnt = arcpy.CreateObject("Point")
            pnt.X = lng
            pnt.Y = lat

            feat = cur.newRow()
            feat.shape = pnt
            feat.setValue("CONFIDENCEVALUE",con)
            cur.insertRow(feat)
            print 'Insert Complete! Total ' + str(count) + " points are inserted! "
            count = count +1
    del cur
    print 'Insert Complete! Total ' + str(count) + " points are inserted! "
        
        
    f.close()
    
except Exception, e:
    print e
    print arcpy.GetMessages()
