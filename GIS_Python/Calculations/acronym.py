# Jon Nordling
# GEOG656
# December 9, 2012

# acronym.py  

# This is the main function that will call function and 
# print the Acronym for the string a user implements 
def main():
	s = raw_input('Enter a phrase: ')
	s_upper = make_upper_case(s)
	results = make_abr(s_upper)
	print 'Acronym: ',results

#This function gets the first character of the string passed
def get_first(string):
	return string[0]

#This to string passed to the function will return upercase
def make_upper_case(string):
	return string.upper()
#This function passes a string and return a list 
def word_to_list(string):
	new_list = string.split()
	return new_list
#This function joins the items in a list to a string
def list_to_string(L):
	return ''.join(L)
# This function creates an creats abrevetion of the string passed
def make_abr(string):
	abr = []
	words = word_to_list(string)
	# Appends the words to the array
	for i in words:
		abr.append(get_first(i))
	#Return call the function that converts a list to a sting
	#resulting in the Abreveation
	return list_to_string(abr)



# This function insures that the main function will exicute first
if __name__ == '__main__':
	main()
