#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

def do_we_keep_going(string_to_test):
    """determine if we are quitting"""
    # normalize our input
    string_to_test = string_to_test.lower()

    if string_to_test == 'q' or string_to_test == "quit":
        return False # it is time to quit
    elif string_to_test.replace(".", "", 1).isnumeric():
        return float(string_to_test) # we do not want to quit, the data is good
    else:
        return False # we are not returning a string

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

        calc1 = do_we_keep_going(calc1)
        # if our function returns FALSE we want to quit (we do not keep going)
        if not calc1:
            break

        # as long as calc2 does not have a value, keep asking the question
        while not calc2:
            print("\nWhat is the second operator? Or, enter q to quit: ")
            calc2 = input()

        calc2 = do_we_keep_going(calc2)
        # if our function returns FALSE we want to quit (we do not keep going)
        if not calc2:
            break

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
