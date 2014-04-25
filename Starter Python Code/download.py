import urllib
dw='UMD.png'
f = urllib.urlopen('http://blaze.umd.edu/images/'+dw)
localFile = open('./'+dw, 'wb')
localFile.write(f.read())
localFile.close()
# Read from the object, storing the page's contents in 's'.

f.close()

