# fibonacci.py
# Jon Nordling

# This program will allow a user to enter a number
# and the program will return the fibnacci number
# To see the same program but using recurive function
# please see fibonacci_recursive.py

def main():
    welcome()        # prompts the welcome function to introduce the program
    check = True     # sets check to true this will be used alow for the program to be run again
    while check is True:
        user_i = user_input()   # gets teh user imput
        fib = get_fib(user_i)   # calls the get_fib() function to calculate the value
        print 'Entered Value  :',user_i
        print 'Fibonacci Value: ',fib
        check = continue_check()        # calls a fuction to check is the user wants to continue

# This function uses temp variable and a loop to determine the value
def get_fib(n):
    fib = 0
    fib_1 = 1
    fib_2 = 0
    temp = 0
    for i in range(n):
        fib = fib_2 + fib_1
        fib_1,fib_2 = fib,temp
        temp = fib_1
    return fib

# This function determines the user imput and makes sure the value is valid
def user_input():
    error = '[INVALID ENTRY]- Try Again'
    while True:
        try:
            user_input = input("Enter number: ")
            print '\n'
            break
        except:
            print error
    return user_input

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
    print'** fibonacci.py                                         *'
    print'** Directions:                                          *'
    print'**            This program asks the user to enter a     *'
    print'**            numner and convert the number into the    *'
    print'**            fibonacci number                          *'
    print'**                                                      *'                                                 
    print x
    print x
    print ' '

## This makes sure that the first funtion called in the main() function
if __name__=="__main__":
    main()
