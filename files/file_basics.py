#!/usr/bin/env python3 
""" 
    How to check if a file exists and what type of file it is
    https://github.com/rentes/python3-code-snippets/blob/master/files/file_basics.py
    Author: Miguel Rentes
    Python version: 3.7.4
"""

# Wrap the file path in an Path object
from pathlib import Path
my_file = Path('/path/to/file')
if my_file.is_file():
  print ("File " + my_file.name + " exists!")
  pass

# How to check what type of file my_file is
# Check https://docs.python.org/3/library/pathlib.html for more goodies
print(my_file.is_dir()) # True if the path is a directory, False otherwise
print(my_file.is_mount()) # True if the path is a mount point, False otherwise
print(my_file.is_symlink()) # True if the path points to a symbolic link, False otherwise
print(my_file.is_socket()) # True if the path is a socket, False otherwise
print(my_file.is_fifo()) # True if the path is a FIFO, False otherwise
print(my_file.is_block_device()) # True if the path is a block device, False otherwise
print(my_file.is_char_device()) # True if the path is a character device, False otherwise
