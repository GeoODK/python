########################3 
## Image Tag program for Pakistan Field work
## Ahmad 

import exifread
import os
import glob
import csv

directory = './'
lng_tag = 'GPS GPSLongitude'
lat_tag = 'GPS GPSLatitude'
alt_tag = 'GPS GPSAltitude'
image_dir_tag = 'GPS GPSImgDirection'

block='12'
csv_file = 'Pictures_12.csv'
out_put_csv = 'outputblock_12.csv'

def get_image_id(i):
	return i[4:-4]

def get_value(lng_value):
	lng =str(lng_value)
	lng = lng.replace("[", "")
	lng = lng.replace("]", "")
	lng = lng.split(',')
	for i in range(len(lng)):
		lng[i]= lng[i].replace(" ","")
		if i == 0:
			#print 'degrees: '+lng[i]
			degrees = float(lng[i])
		if i == 1:
			#print 'minutes: '+ lng[i]
			minutes = float(lng[i]) / 60
		if i == 2:
			temp = lng[i].split('/')
			seconds = float(temp[0])/float(temp[1])
			seconds = seconds / 3600
	value = degrees+minutes+seconds
	return value

def get_alt(a):
	a = str(a)
	t = a.split('/')
	if len(t)<2:
		alt = t[0]
	else:
		alt = float(t[0])/float(t[1])
	return alt

def main():
	out_put = open(out_put_csv,'wb')
	row1 = "Block ID,Picture ID,Longitude,Latitude,Altitude,Image Direction"+'\n'
	out_put.write(row1)
	for image in glob.glob("*.JPG"):
		f = open(image,'rb')
		image_id = get_image_id(image)		
		print image_id
		tags = exifread.process_file(f)
		for tag in tags.keys():
			if tag ==lng_tag:
				lng =get_value(tags[tag])
			if tag == lat_tag:
				lat= get_value(tags[tag])
			if tag == alt_tag:
				alt = get_alt(tags[tag])
			if tag == image_dir_tag:
				dir_tag = get_alt(tags[tag])
		string = str(block)+','+str(image_id)+','+str(lng)+','+str(lat)+','+str(alt)+','+str(dir_tag)+'\n'
		out_put.write(string)
	out_put.close()
		


def csv_go(csv_file):
	with open(csv_file, 'rb') as fp:
		a = csv.reader(fp, delimiter=',')
		for row in a:
			print row


if __name__ == '__main__':
	main()