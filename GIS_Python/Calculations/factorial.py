# factorial.py
# Jon Nordling
# Description: Program to determine the factorial of a number passed by a user


## This is the main function
# Is calls the functions needed for the program
# Also checkes to see if the use would like to continue
# or to exit the program

def main():
    welcome()       # The welcome() function displays the directions and author of the program
    check = True    # Define the check to be true at start
    #The following while loop runs the main function as long a check = true
    while check  is True:
        x = user_input()    # The function defines the user imput
        factor = calc(x)    # This function will calcuate the factorial of the user input
        print 'The factorial of ' + str(x) + ' is:', factor
        print ' '        
        check = continue_check()    # This function defines if the user wants to continue the program

# The following function will determine is the user will want to continue the program of not
# if the user does not want to continue the program will return false else it will return true
def continue_check():
    error = '[VALUE INVALID]-Please Enter- (y/n)'   # Defines the error message
    test = True       # sets the test variable to True
    while test is True:
        test = raw_input('Enter Another number?(y/n): ')    # Prompts the user
        if (test =='n') or (test =='no'):
            # If the user does not want to continue test is set as False
            test = False
            print 'Good by........' 
        elif (test =='y') or (test =='yes'):
            # if the user wants to continue sets test to True and breaks the loop
            test = True
            break
        else:
            #This is if the user enters any other answer the program will signal an error and
            # sets test to be true so the user will be prompted again
            test = True
            print error
    return test

## The calc function takes one paramiter (a whole number)
# then caclucated the factorial of the numnber
# the number will be a data type lone
def calc(num):
    value = 1L          # defines the valuse as a long
    num = int(num)      # insures that the number passed is a integer
    # The loop defines the factorial of the number passed to the fubction
    for i in range(num, 0, -1):
        value = value * i
    return value

## The user_input function asked the to enter a whole numner
# If the number is not valid it will say so else the fuction
# will retrurn the main function

def user_input():
    error = '[VALUE INVALID]-Only Whole numbers'    # defines the error message to the user
    
    while True:
        # using a try operator to promte the user which will help single invaled entrys
        try:
            user_input = input('Please enter a whole number: ') # Prompts the user for a number
            test = float(user_input % 1)    # uses a mod to determine if the value entered is a decimal          
            if test > 0 :
                # If the number a decimal then signal error
                print error
            else:
                # If the entry is valid then break the loop
                break
        except:
            # if any error is found then signal the error message
            print error
    return user_input


## This is the welcome screan that will only be displayed once
# at the begining of the program

def welcome():
    x = '*********************************************************'
    print x
    print x
    print'** Universtiy of Maryland                               *'
    print'** By Jon Nordling                                      *'
    print'**                                                      *'
    print'** factorial.py                                         *'
    print'** Directions:                                          *'
    print'**            This program asks the user to enter a     *'
    print'**            number (which must be a whole number)     *'
    print'**            then will return its factorial.           *'
    print'**                                                      *'                                                 
    print x
    print x
    print ' '
    
## This makes sure that the first funtion called in the main() function
if __name__=="__main__":
    main()
