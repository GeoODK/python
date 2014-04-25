#print "\nReading the entire file into a list."
text_file = open("cool.txt", "r")
lines = text_file.readlines()
#print lines
#print len(lines)
for line in lines:
    print line
text_file.close()

