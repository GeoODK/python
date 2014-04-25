# This is an exercise file from Geog656

earth_line = 0
file = open("data.txt", "r")

for line in file:
    line = line.strip()    

    earth_line = earth_line + 1       
    if line == "Earth":    
        break
     
    
print "Earth is at line %d" % earth_line
