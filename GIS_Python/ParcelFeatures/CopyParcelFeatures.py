# CopyParcelFeatures.py
# Description: Extracts Austin Housing Authority owned parcels
# Author: Jon Nordling
# Date: 01/24/13

import arcpy

try:
    arcpy.env.workspace=r'./'
    arcpy.MakeFeatureLayer_management("coa_parcels.shp", "lyr")
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "\"PY_FULL_OW\" = \'AUSTIN HOUSING AUTHORITY\'")
    arcpy.CopyFeatures_management("lyr", "hsng_auth2")
    print 'New Feature Class created'
except Exception, e:
    print e   #e is a variable the refers to an Exception object
    print arcpy.GetMessages()
    arcpy.AddError(e)
