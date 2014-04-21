# Date: 04/19/2014
# Author: Jon Nordling
# Purpose:
# Main program for running code to download and proces class Data

# Library need to run script

import os
import sys
import glob
from datetime import date, timedelta
from modules.HDF5_Reader_CLASS import *
from modules.FTP_Download_CLASS import *

# Define the array of dates/day to download
# To download yesturdays data
# Note: The date is how Class's FTP structure is defined

yesturday_date = str((date.today()-timedelta(1))).replace("-","")

date = ["20140416","20140417"]
#date = [yesturday_date]

scratch_dir = '/home/jnordling/Class/scratch/'
output_dir = '/home/jnordling/Class/output/'

for d in date:
	# Download the Data
	ftp = FTP_Download(date=d,scratch_directory=scratch_dir)
	ftp.download()

	# Create file and write first row.
	op_string =output_dir+d+"_Global_CLASS.txt"
	output_file = open(op_string,"wb")
	output_file.write("year,month,day,latitude,longitude"+'\n')

	# Process HDF5 Class
	hdf_files = glob.glob(scratch_dir+"*.h5")
	for i in hdf_files:
		print i
		output_file.close()
		# Append Detections on to file
		process = Hdf_Class(i,op_string)
	# Remove left over files
	os.system("rm -rf "+scratch_dir+"*")
print 'Complete'
#files = Hdf_Class(fil,output_file)