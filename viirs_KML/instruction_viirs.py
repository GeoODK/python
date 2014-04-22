# Jon Nordling 
# University of Maryland
# Graduate Research Assistant 
# 08/10/2012

#######################################
# This is a python program that converts a text file with lat, lng cordinatons into a 
# Google earth/map format kml/kmz. The program uses a 3rd party module called simpleKml
# Download the folder to test the program. Must install simplekml first
# For Python 2.6 or higher
#######################################
# Sets the imports needed for the program

import os
import sys
import simplekml

#Setting the Global variables
# Loc = the directory where the text files are located
# files = the list of files in that directory 

loc = './'
files = ['NPP_VIIRS_20140111_AF.txt','NPP_VIIRS_20140112_AF.txt']

# The following function is the main function that will be the first
# function run when the program is launched

def main():
	# loops through each of the files
	for i in files:
		kml = simplekml.Kml()				# Launch the Kml Object
		in_file = open(i)					# Open the file
		file_lines = in_file.readlines()	# retrieves each of the lines in the file
		num_lines = len(file_lines)			# Sets a variable to the number of lines in the file

		for j in range(1, num_lines):		#Loop through each of the lines in the file
			# pnt = the lat and lng points that located on the line of text file. 
			# Reference the text file to see format to fullly understanding
			
			pnt = kml.newpoint(coords=[(get_lng(j), get_lat(j))])		# Call the lat and lng functions to retreive the values
			pnt.style.iconstyle.icon.href = 'fireicon.png'				# Defines the icon that will display in the kml file(not required)
			pnt.style.iconstyle.scale = 1								# Defines the icon scale(not required)

	kml.savekmz(i[0:21]+'.kmz')				# Saves a a kmz file. (To save as kml replace line with kml.save(i[0:21]+'.kml'))
	in_file.close()							#Close the file
	
	
	
	
# function gets the lng from the file and line numnber passed
def get_lng(line):
    line = file_lines[line].strip()		# create an array of all the values in the line
    lng = line[23:33]					# Locateds and defines the lng
    return lng							# Retuns the lng

# function gets the lat from the file and line numnber passed
def get_lat(line):
    line = file_lines[line].strip()		# create a array of all the values in the line
    lat = line[34:]						# Locateds and defines the lat
    return lat							# Retuns the lat















