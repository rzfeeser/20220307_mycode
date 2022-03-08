#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

def do_we_keep_going(string_to_test):
    """determine if we are quitting"""
    # normalize our input
    string_to_test = string_to_test.lower()

    if string_to_test == 'q' or string_to_test == "quit":
        return (False, "You indicated you want to quit. Good-bye")# it is time to quit
    elif string_to_test.replace(".", "", 1).isnumeric():
        return True # we do not want to quit, the data is good

def main():
    """run time code"""

    while True:

        calc1 = ""
        calc2 = ""
        operation = ""
        
        # as long as calc1 does not have a value, keep asking the question
        while not calc1:
            print("\nWhat is the first operator? Or, enter q to quit: ")
            calc1 = input()

        # did they give us a value to exit
        if calc1 == "q":
            break
        elif not calc1.replace(".", "", 1).isnumeric():  # this will eval to false when we want to end
            print("You did not give me a number")
            break

        
        # convert calc1 safely to a float
        calc1 = float(calc1)

        ###### We need a function to "fix" this repeating code issue ######

        # as long as calc2 does not have a value, keep asking the question
        while not calc2:
            print("\nWhat is the second operator? Or, enter q to quit: ")
            calc2 = input()

        # did they give us a value to exit
        if calc2 == "q":
            break
        elif not calc2.replace(".", "", 1).isnumeric():
            print("You did not give me a number")
            break


        # convert calc2 safely to a float
        calc2 = float(calc2)


        ### collect operation ###
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()
        

        # check operation
        if operation == "+":
            # print(\n + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
            print(f'\n{calc1} + {calc2} = {calc1 + calc2}')

        elif operation == '-':
            #print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
            print(f'\n{calc1} - {calc2} = {calc1 - calc2}')
        else:
            print("\n Not a valid entry. Restarting...")


if __name__ == "__main__":
    main()
