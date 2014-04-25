# InsertWildfires_part2.py
# Purpose: The purpose of this program is to create a point feature in the WildlandsFires.mdb that will
#          contain the atributed of Latitude, Longitude, Confidence. The spacial reference of the 
#          the new feature will contain the same one as the FireIncidents in the .mdb
# Author: Jon Nordling
# Date: 02/06/13


import arcpy
import os

# This is a function that adds fields to the feature
# based on the header array passed
def add_HeaderFields(header):
    for i in header:
        arcpy.management.AddField(out_name, i, "DOUBLE")
        print 'Field Added: ' + i

# This function it to get the workspace the user specifies 
def get_workspace():
    path = raw_input("Specify the full path of WildlandFires.mdb: ")
    return path
    
# This function is to get the name of the new feature created
def get_out_name():
    name = raw_input('Enter the output name: ')
    return name

# This funtion gets that file that contains the lat\lng information
def get_file():
    file_name = raw_input('Specify the wildland fire file with full path: ')
    return file_name

# This is to remove the new line charaters from and array
# The function return the array with out the newline
def remove_new_line(array):
    new_array = []
    for j in array:
        if '\n' in j:
            x= j.strip('\n')
            new_array.append(x.upper())
        else:
            new_array.append(j.upper())
    return new_array

# This is the main funtion that will control tha main processes of the program
def main():

    try:
        # These are declaring input variables
        out_path = get_workspace()
        input_file = get_file()

        # This variable is being created as Global 
        # Will be used in a function in another process
        global out_name     
        out_name = get_out_name()

        # Set the arcpy workspace
        arcpy.env.workspace=out_path
        print ' '

        # These variables are setting the parameters of the new feature called
        geometry_type = "POINT"
        spatial_reference = arcpy.Describe("FireIncidents").spatialReference
        template = ""
        has_m = "DISABLED"
        has_z = "DISABLED"

        # Creating the new feature
        arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)
        print 'Feature Class Create: ' + out_name

        # opening the file with the r for read only
        f = open(input_file, 'r')
        lstFires = f.readlines()

        count = 0

        # This loop goes through each line of the file and inserts the headers as attribute fields
        # Then for all the other lines it will pars the latitude, longitude, confident level and 
        # insert them into the new feature, as a point. 
        for i in lstFires:
            if count==0:
                # The first row of the file, creates the header and 
                # Creates the Insert Cursor
                header = remove_new_line(i.split(","))
                add_HeaderFields(header)
                rows = arcpy.InsertCursor(out_name)
            else:
                # gets the data into vaiables. and createing a point object
                line = remove_new_line(i.split(","))
                lat = line[0]
                lng = line[1]
                cof = line[2]
                pnt = arcpy.CreateObject("Point")
                pnt.X = lng
                pnt.Y = lat

                # Inserting the data into the rows
                row =rows.newRow()
                row.shape = pnt
                row.setValue(str(header[0]),lat)
                row.setValue(str(header[1]),lng)
                row.setValue(str(header[2]),cof)
                rows.insertRow(row)
                print'Insert Row Complete: '+ str(count)
            # Increasing the count
            count = count + 1
        print "Insert Complete! Total " + str(count-1) + " points are inserted!\n" 
        # These dump the variable memory 
        del rows
        del row
        # Closes the open file
        f.close()
    except Exception, e:
        # Catching Errors it program fails
        print e
        print arcpy.GetMessages()


# This calls the main function first
if __name__ == '__main__':
    main()
