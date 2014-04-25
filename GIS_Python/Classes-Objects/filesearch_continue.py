# This is an exercise file from Geog656

earth_line = 1
file = open("fileinput_continue_data.txt", "r")

for line in file:
    line = line.strip()
    
    if line.startswith("#"):
        continue
    if line == "Earth":
        break
    earth_line = earth_line + 1

print "Earth is at line %d" % earth_line
