# Jon Nordling
# GEOG653 
# December 9, 2012

# stat.py
import math

# Return the largest number in a list
def get_max(alist):
	return max(alist)

# Returns the smallest number in a list
def get_min(alist):
	return min(alist)

# Returns the sum of the list
def get_sum(alist):
	return sum(alist)

# Returns the length of the list
def get_len(alist):
	return len(alist)

# Returns the mean of the list
def getMean(alist):
	return sum(alist)/float(get_len(alist))

# Returns the Standard Deveation of the list
def getStdv(alist):
	sd = math.sqrt(sum((x-getMean(alist))**2 for x in alist)/get_len(alist))
	return sd

# Returns a list sorted in Acending order
def ascend(alist):
	return sorted(alist)

# Return a list sorted in Decending order
def descend(alist):
	return sorted(alist, reverse=True)

#This is the main function that contains the list
# Also will print the max,min,average,standard, 
# deveation, and the list in  acending and decending
# order
def main():
	c = [2123, 1284, 7031, 30788, 147, 2217, 10000]
	print ' '
	print 'Maximum Population: ', '%.0f' % get_max(c)
	print 'Minimum Population: ', '%.0f' % get_min(c)
	print 'Average Population: ', '%.2f' % getMean(c)
	print 'Standard Deviation: ', '%.2f' % getStdv(c)
	print 'Total Population:   ', '%.2f' % get_sum(c)
	print ' '
	print 'Populations:     ', c
	print 'Ascending Order: ', ascend(c)
	print 'Decending Order: ', descend(c)
	print ' '



# This function insures that the main function will exicute first
if __name__ == '__main__':
	main()
