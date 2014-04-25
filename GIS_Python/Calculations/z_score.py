# GEOG 656
# Jon Nordling
# The files need for this program are all in the zip file

import os
import math

input_file = './Lab3_Data/NCSIDS_ObsExp.txt'
z_output_file = './Lab3_Data/NCSIDS_ObsExp_Zscore.txt'
chisquare_file = './Lab3_Data/chisquare.txt'

# This is the main function that will call and format
# the outputs to the screan.
# The main functionality of the program will create a new file
# with the corosponding z-score valuse
# Then determine the observed chi, degree of fredom,
# and signal to except or reject the null hypothesis

def main(): 
    create_z_file()
    ob_chi,df = calc_chi()
    critical_chi = confidence(df)
    hypothes_test = hypoth_test(ob_chi,critical_chi)
    print 'Observed Chi Value:', '%0.2f' % ob_chi
    print 'Degree of Fredom  :', df
    print 'Critical Chi Value:',critical_chi
    print 'The null hypothesis of no spatial pattern:',hypothes_test

##################
# Part One  60pt
##################
# This function creates a file that will include everything from the 
# input file however there will be a new field added that include
# the z score value. There are helper function inside the function
# to assist with calculating the z value
def create_z_file():
    def clean_node_nl(string):
        # This function takes a sting and remove the new line character
       return string.strip('\n')
    def clean_node_space(string):
        # This function takes a sting and remove the space character
        return string.strip(' ')
    def calc_z(ob,ep):
        # This function calcualed the z score using math functions
        z = (int(ob)-int(ep))/(math.sqrt(int(ep)))
        return z
    try:
        # The following code will read input file and 
        # create the output file with the zscore value in it
        f = open(input_file, 'r')
        o = open(z_output_file, 'w')
        all_lines = f.readlines()
    
        counter = 0
        for i in all_lines:
            counter = counter +1
            line = i.split(',')
            country_name = str(line[0])
            x_cords = line[1]
            y_cords = line[2]
            ob = clean_node_space(line[3])
            ep = clean_node_space(clean_node_nl(line[4]))
            z = '%0.4f' % calc_z(ob,ep)
            phrase = country_name +','+x_cords+','+ y_cords+','+ob+','+ep+','+z
            if counter == len(all_lines):
                new_line = phrase
            else:
                new_line = phrase + '\n'
            o.write(new_line)
        f.close()
        o.close()
    except:
        # If an error occurs this error message will return
        print 'Error with file'

###############
# Part 2 20pt
###############
# This function calcualtes the chi value and the degree of fredom
# there is a math function in the function 
# to calcualte the value.
# The function will return the chi valuse and the degree of fredom

def calc_chi():
    def calc_chi_value(array):
        chi_array = []
        for p in array:
            chi = chi_array.append(float(p)**2)
        return sum(chi_array)
    z_file = open(z_output_file, 'r')
    all_z_lines = z_file.readlines()
    z_array= []
    for j in all_z_lines:
        line = j.split(',')
        z_array.append(line[-1].strip('\n'))
    
    chi = calc_chi_value(z_array)
    df = len(all_z_lines)-1
    return chi,df

###############
# Part 3 20pt
###############
# This function will determine the confidence level and return the critical Chi
# This function uses a file provided in the zip folder
def confidence(df):
    f = open(chisquare_file, 'r')
    lines = f.readlines()
    critical_chi = ''
    for i in lines:
        line = i.split('  ')
        if line[0] == str(df):
            critical_chi = line[1]
    f.close()
    return critical_chi
# This function tests the observed value and the critical chi to 
# determine if we sould except or reject the null hypothesis
def hypoth_test(ob,critical_chi):
    if float(ob) >= float(critical_chi):
        return 'is rejected'.upper()
    else:
        return 'cannot be rejected.'.upper()
    

# This function insures that the main function will exicute first
if __name__ == '__main__':
	main()


































	
