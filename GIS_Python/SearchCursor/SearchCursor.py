# SearchCursor.py
# Purpose: The purpose of this program is to use the searchCursor to find the schools that are highschool in the set shape file
# Author: Jon Nordling
# Date: 01/31/13

import arcpy


try:
    # The following code excepts a user input to set the workspace
    arcpy.env.workspace= raw_input("Enter your workspace will full path: ")

    # The following code creates a searchCursor to search the shape file for High Schools
    searchCurs = arcpy.SearchCursor("Schools.shp","\"FACILITY\" = \'HIGH SCHOOL\'")

    # The row variable starts and sets the values of the row of the atributes that are
    # contained from the search
    row = searchCurs.next()

    # This is a loop loops though all the records and prints out the name
    # Then sets the row to the next row
    # The loop will finish when there are no more records
    while row:
        print row.getValue("NAME")
        row = searchCurs.next()
except:
    # This code will print out the arcpy error that is cought
    print arcpy.GetMessage()
