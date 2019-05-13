#!/usr/bin/env python3
"""
    Global vs Local variables
    Author: Miguel Rentes
    github.com/rentes/python3-code-snippets/blob/master/variables/nonlocal_variable.py
    Python version: 3.7.2
    A nonlocal variable lets you assign values to a variable in an outer (but non-global) scope
"""
def F(first_parameter, second_parameter):
    """ 
        A function that receives two parameters
        The two parameters are also local variables
    """
    variableA = "local"
    print('local variableA value: ', variableA)

    def inner():
        """
        Inner function
        """
        nonlocal variableA # exactly the same variable as in line 14
        variableA = "nonlocal"
        print('local variableA value inside inner function: ', variableA)
    
    inner()
    print('local variableA value: ', variableA)


if __name__ == "__main__":
    F(1, 2)