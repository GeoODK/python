import os
f = open('file.html', 'w')
localFile = open('file.html', 'w')
localFile.write('<!-')
localFile.write('By Jon Nordling\n')
localFile.write('Date-Time-Information\n')
localFile.write('Geog384 Internship\n')
localFile.write('-->\n\n\n')
localFile.write(f.read())
f.close()

localFile.close()
