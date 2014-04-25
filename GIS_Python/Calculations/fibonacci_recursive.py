# fibonacci_recursive.py
# Jon Nordling

# This program will allow a user to enter a number
# and the program will return the fibnacci number
# NOTE: This program calcuates the fibonacci valuse using recursion

def main():
    welcome()        # prompts the welcome function to introduce the program
    check = True     # sets check to true this will be used alow for the program to be run again
    while check is True:
        user_i = user_input()
        index_list = list(xrange(user_i+1)) # this creates a list of the numbers entered by the user
        fib = get_f(index_list)
        print 'Entered Value  :',user_i
        print 'Fibonacci Value: ',fib
        check = continue_check()        # calls a fuction to check is the user wants to continue

# This function used array and recursion to define the fibonacci valuse
# The function takes in a list
def get_f(list_num):
    f_array = []    # This will define the fibonacci array
    for j in list_num:
        if j == 0:
            f_array.append(0)
        elif (j ==1) or (j ==2):
            f_array.append(1)
        else:
            # uses recursion to get the valuse stored
            f_array.append(f_array[j-1]+f_array[j-2])
    return f_array[-1]
# This function gets the user imput
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
    print'** fibonacci_recursive.py                               *'
    print'** Directions:                                          *'
    print'**            This program asks the user to enter a     *'
    print'**            numner and convert the number into the    *'
    print'**            fibonacci number                          *'
    print'** NOTE: This program calcuates the fibonacci valuse    *'
    print '        using recursion                                *'
    print'**                                                      *'                                                 
    print x
    print x
    print ' '

## This makes sure that the first funtion called in the main() function
if __name__=="__main__":
    main()
