import urllib

f = urllib.urlopen("http://www.wunderground.com/history/station/31939/2005/3/1/MonthlyHistory.html")

localFile = open('file.html', 'w')
localFile.write(f.read())
localFile.close()
# Read from the object, storing the page's contents in 's'.

f.close()

