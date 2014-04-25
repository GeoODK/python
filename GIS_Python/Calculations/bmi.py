# Jon Nordling 
# GEOG656 Python Programing
# December 9, 2012

# bmi.py

# This is the main function that will call function and 
# print the bim of the user imputs
def main():
	bmi = calc_bmi()
	result = bmi_means(bmi)
	print 'You are: ',result
# This function will determine the users Weight and hight
# and calculate there bmi
def calc_bmi():
	w = input('Enter your Weight: ')
	h = input('Enter Height: ')
	bmi = (w*703)/(h*h)
	return bmi

# This function passed the bim and then 
# Determines the output
def bmi_means(bmi):
	if bmi < 18.5:
		r = 'Under Weight'
	elif bmi >= 18.5 and bmi <25:
		r = 'Healthy Weight'
	elif bmi >=25 and bmi <30:
		r = 'Over Weight'
	else:
		r = 'obesity'
	return r  

# This function insures that the main function will exicute first
if __name__ == '__main__':
	main()

