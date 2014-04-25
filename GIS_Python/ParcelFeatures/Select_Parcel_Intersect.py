# Select_Parcel_Intersect.py
# Description: 
# Author: Jon Nordling
# Date: 01/24/13

import arcpy
try:
    #workspace = 'C:\Users\jnordling\Dropbox\GEOG656\Lab6\lab6_data'
    #input_parcels = './lab6_data/coa_parcels.shp'
    #input_flood_plains = './lab6_data/Floodplains.shp'
    #output = 'selectedParcels.shp'

    workspace = arcpy.GetParameterAsText(0)
    input_parcels = arcpy.GetParameterAsText(1)
    input_flood_plains = arcpy.GetParameterAsText(2)
    output = arcpy.GetParameterAsText(3)

    arcpy.env.workspace= workspace
    arcpy.MakeFeatureLayer_management(input_parcels, "parcel_lyr")
    arcpy.SelectLayerByLocation_management ("parcel_lyr", "INTERSECT",input_flood_plains )
    arcpy.CopyFeatures_management("parcel_lyr", output)
    print 'New Feature Class created'
    
    
except Exception, e:
    print e   #e is a variable the refers to an Exception object
    print arcpy.GetMessages()
    arcpy.AddError(e)
