import urllib
import os.path
import os


location = '/Users/jon/Library/Caches/Google/Chrome/Default/Cache/'
output = '/Users/jon/Desktop/cache/'

for filename in os.listdir(location):
	print location+filename
	
	f = urllib.urlopen(location+filename)
	localFile = open(output+filename, 'w')
	localFile.write(f.read())
	localFile.close()
	f.close()

#for filename in os.listdir(location):
#   print  filename
 



