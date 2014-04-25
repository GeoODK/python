# SearchCursor.py
# Purpose: The purpose of this program is to find the names of the hospitals in the user-specified 5-digit zip code areas. 
# Author: Jon Nordling
# Date: 01/31/13

import arcpy

try:
    # The following code excepts a user input to set the workspace
    arcpy.env.workspace= raw_input("Enter your workspace will full path: ")

    # This is a test variable to be used to validate the zipcode entered from the user
    test = True
    while test == True:

        # This gets the zipcode from the user
        zipcode = raw_input("Enter Zipe Code: ")

        # The following code creates a searchCursor
        searchCurs = arcpy.SearchCursor("Hospitals.shp","\"ZIPCODE\" LIKE \'"+zipcode+"%\'")
        
        # The row variable starts and sets the values of the row of the atributes that are
        # contained from the search
        row = searchCurs.next()

        # This is a test function to test if the row is empty or not and if it is ask for another one
        if row != None:
            test = False
        else:
            print '[Error] No Hospitals near that Zip Code'
            print 'Try Again'
            print ' '

    
    # This loop gets tha name of the hospial from reach row and prints them out
    count =0
    while row:
        print row.getValue("NAME")
        row = searchCurs.next()
        count = count+1
    print ' '
    print 'Total number of Hospitals found: ', count
except:
    # This code will print out the arcpy error that is cought
    print arcpy.GetMessage()
