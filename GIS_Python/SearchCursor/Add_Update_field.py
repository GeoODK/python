# Add_Update_Field.py
# Purpose: The purpose of this program is to use the Update Curors to create a new field with containing the hole address
#          which is dirived from other fields
# Author: Jon Nordling
# Date: 01/31/13


import arcpy

try:
    # The following code excepts a user input to set the workspace
    arcpy.env.workspace= raw_input("Enter your workspace will full path: ")

    # The following code creates a new field in the shape file with defines name and data type/size
    arcpy.management.AddField("Hospitals.shp", "FullAddr","Text", "50")

    # This variable is set to create the UpdateCursor
    updCursor = arcpy.UpdateCursor("Hospitals.shp")

    # The row variable starts and sets the values of the row
    row = updCursor.next()

    # A counter variable
    count = 0

    # This while loop will loop through all the rows
    while row:

        # The values are the represent the valuse in the colums of the row(attributes)
        strAddress = row.getValue("ADDRESS")
        strCity = row.getValue("CITY")
        strState = row.getValue("STATE")
        strZip = row.getValue("ZIPCODE")

        # This variable is set to create a string the full address
        strFullAddress = strAddress +','+ strCity + ',' + strState + ","+ strZip

        # The following sets above variable to the FullAddr field
        row.setValue("FullAddr",strFullAddress)

        # This updates the row
        updCursor.updateRow(row)

        # Increases the count
        count = count+1

        print "Update record number: " + str(count)
        row = updCursor.next()
    print 'Update Complete'

    # This deletes the variable for memory purposes
    del updCursor
except:
    print arcpy.GetMessage()
