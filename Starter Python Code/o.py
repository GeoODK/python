import simplekml
import os
os.chdir("C:\Users\jnordling\Desktop")
kml = simplekml.Kml()
pnt = kml.newpoint(name='Point')
pnt.coords = (37.999,-94.834)
pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
kml.save("Styleeee.kml")
