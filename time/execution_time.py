#!/usr/bin/env python3 
""" 
    How to get the time it takes for a Python code block to execute?
    https://github.com/rentes/python3-code-snippets/blob/master/time/execution_time.py
    Author: Miguel Rentes
    Python version: 3.7.4
"""
import time

start_time = time.time()

# Your code block starts here
#  😴😴😴
# End of your code block which you want to know how long it took to run 

print("This code block took %.3f seconds to run" % (time.time() - start_time))