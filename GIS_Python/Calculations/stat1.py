# Jon Nordling
# GEOG653 
# December 9, 2012

# stat1.py
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
	return sum(alist)/float(len(alist))

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

# This function is to create an array of the numbers 
# entered by the user. The function checks for valid 
# entrys 
def getCollectedData():
	array = []
	while True:
		try:
			value = input('Enter Value: ')
			if value == -1:
				break
			elif value > 0:
				array.append(value)
			else:
				print 'Try Again'
		except:
			print 'Error'
	return array

# This is the main function is the main function
# Also will print the max,min,average,standard, 
# deveation, and the list in  acending and decending
# order
def main():
	c = getCollectedData()
	print ' '
	print 'Populations:     ', c
	print ' '
	print 'Maximum Population: ', '%.0f' % get_max(c)
	print 'Minimum Population: ', '%.0f'   % get_min(c)
	print 'Average Population: ', '%.2f' % getMean(c)
	print 'Standard Deviation: ', '%.2f' % getStdv(c)
	print 'Total Population:   ', '%.2f' % get_sum(c)
	print ' '
	print 'Ascending Order: ', ascend(c)
	print 'Decending Order: ', descend(c)
	print ' '




if __name__ == '__main__':
	main()
