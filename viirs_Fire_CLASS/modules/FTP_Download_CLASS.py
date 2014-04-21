# Date: 04/19/2014
# Author: Jon Nordling
# Purpose:
# Module used for downloading data from CLASS FTP

import ftplib
import os
import glob
import subprocess
from datetime import date,timedelta#

class FTP_Download():
    """docstring for FTP_Download"""
    def __init__(self,date,scratch_directory):
        self.date = date
        self.scratch_directory = scratch_directory

    def download(self):

        ftp = ftplib.FTP('ftp-npp.class.ngdc.noaa.gov')
        ftp.login()
        dirlist = ftp.nlst() # Gets the list of directories of FTP

        for d in dirlist:
            if d ==self.date:
                ftp.cwd(d+'/VIIRS/VIIRS-Active-Fires-ARP') # change FTP directory to a specified folder
                files = ftp.nlst()  # Get list of files new directory
                #print files
                # For each of the files for the files (should be .tar and .xml)
                for i in files:
                    out_putfile = open(self.scratch_directory+i,'wb')
                    ftp.retrbinary('RETR '+i,out_putfile.write) # Download and write file to the scratch directory
                    out_putfile.close() # Close the open file and move to next file
                    # File download
        os.chdir(self.scratch_directory) # Change the directory to scratch folder

        # Get each of the tar files that have been downloaded them
        tar_files = glob.glob('./*.tar')
        print tar_files
        for tar in tar_files:
            #Fow each of the tar file begin subprocess that unzips it
            x = subprocess.Popen(["tar","-xvf",tar])
            x.wait() # wait before subprocess is complete unziping

        # Unconpress the .gz files
        gz_file = glob.glob("./*.gz")
        for gz in gz_file:
            #subprocess(["gunzip",os.getcwd()+'/'+gz])
            # 
            f= self.scratch_directory+os.path.basename(gz)
            p = subprocess.Popen(["gunzip",gz])
            p.wait()
        # Remove un-need files
        os.system("rm -rf "+self.scratch_directory+ "*.tar")
        os.system("rm -rf "+self.scratch_directory+ "*.xml")

        #os.system("python /home/jnordling/Class/modules/python/h5py_reader.py")
        print 'Download Complete'
