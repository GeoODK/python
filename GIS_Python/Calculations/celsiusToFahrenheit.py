# celsiusToFahrenheit.py
# Jon Nordling
# This program will convert Celsius to Fahrenheit


def main():
    welcome()   # prompts the welcome function to introduce the program
    check = True  # sets check to true this will be used alow for the program to be run again
    while check is True:
        user_c = user_input()
        celsius = "%.2f" % round(user_c,2)
        fah = "%.2f" % round(convert(user_c),2)
        print ' '
        print 'Celsius: ' +str(celsius)
        print 'Fahrenheit: ' +str(fah)
        check = continue_check()        # calls a fuction to check is the user wants to continue
    
# This function will convert the passed Celsius temperature to Fahrenheit
# then returns the value
def convert(cel):
    f = (cel * 9.0/5.0)+32.0
    return f

# This function determines the user imput and makes sure the value is valid
def user_input():
    error = '[INVALID ENTRY]- Try Again'
    while True:
        try:
            user_input = input("Enter Celsius temperature: ")
            break
        except:
            print error
    return round(user_input,2)

# The following function will determine is the user will want to continue the program of not
# if the user does not want to continue the program will return false else it will return true
def continue_check():
    print '\n'
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


def welcome():
    x = '*********************************************************'
    print x
    print x
    print'** Universtiy of Maryland                               *'
    print'** By Jon Nordling                                      *'
    print'**                                                      *'
    print'** celsiusToFahrenheit.py                               *'
    print'** Directions:                                          *'
    print'**            This program asks the user to enter a     *'
    print'**            Fahrenheit temperature and convert the    *'
    print'**            the temperature to Celsius.               *'
    print'**                                                      *'                                                 
    print x
    print x
    print ' '
    
## This makes sure that the first funtion called in the main() function
if __name__=="__main__":
    main()
