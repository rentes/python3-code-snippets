#!/usr/bin/env python3
"""
    Global vs Local variables
    Author: Miguel Rentes
    github.com/rentes/python3-code-snippets/blob/master/variables/global_local_variables.py
    Python version: 3.7.2
    globals() and locals() return a dictionary of global and local scope variables respectively
"""
# these are global variables
variableA = 1
variableB = 2

def F(first_parameter, second_parameter):
    """ 
        A function that receives two parameters
        The two parameters are also local variables
    """
    global variableA # this is the global variable at line 10
    variableB = 3 # this is a new local variable (it is NOT the global variable at line 11)
    print('local variables inside function F: ' + str(locals()))
    print('global variables inside function F: ' + str(globals()))

if __name__ == "__main__":
    print('local variables are: ' + str(locals()))
    print('global variables are: ' + str(globals()))
    F(1, 2)
