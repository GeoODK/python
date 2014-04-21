import 	h5py
import datetime
import glob
import os
class Hdf_Class():
	def __init__(self,hdf_file,output_file):
		self.file_name = hdf_file
		self.hdf = h5py.File(self.file_name, "r")
		self.group_attrs = self.hdf['Data_Products']['VIIRS-AF-EDR']['VIIRS-AF-EDR_Aggr'].attrs
		self.num_of_granules = self.group_attrs['AggregateNumberGranules'][0][0]
		self.output_file = output_file
		self.process()

	def process(self):
		op_file = open(self.output_file,"ab")
		index = self.num_of_granules
		for i in range(int(index)):
			date = self.get_date(str(i))
			year = date[:4]
			month = date[4:6]
			day_of_month =date[6:8]
			#time_utc =self.get_time(str(i))
			#time =str(datetime.timedelta(seconds=float(time_utc)))
			#print time
			lat_group = self.hdf['All_Data']['VIIRS-AF-EDR_All']['Latitude']["Latitude_"+str(i)]
			lng_group = self.hdf['All_Data']['VIIRS-AF-EDR_All']['Longitude']["Longitude_"+str(i)]
			for j in range(len(lat_group)):
				op_string = str(year)+','+str(month)+','+str(day_of_month)+','+str(lat_group[j])+','+str(lng_group[j])+'\n'
				op_file.write(op_string)
		op_file.close()

	def get_date(self,index):
		attrs = self.hdf['Data_Products']['VIIRS-AF-EDR']['VIIRS-AF-EDR_Gran_'+index].attrs
		date = attrs['Ending_Date'][0][0]
		return date
	def get_time(self,index):
		attrs = self.hdf['Data_Products']['VIIRS-AF-EDR']['VIIRS-AF-EDR_Gran_'+index].attrs
		time = attrs['Ending_Time'][0][0]
		return time[:6]

