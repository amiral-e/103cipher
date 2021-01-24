##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## errors_man.py
##

import os
from sys import argv
import math
import random
from src.constants import *

def usage(c):
    if (c == 1):
        print("Usage: ./103cipher message key flag")
    else:
        print("USAGE\n    ./103cipher message key flag\n")
        print("DESCRIPTION")
        print("    message\ta message, made of ASCII characters")
        print("    key\t\tthe encryption key, made of ASCII characters")
        print("    flag\t0 for the message to be encrypted, 1 to be decrypted")

def errors(c, num_arg):
    if (c == 1):
        if (num_arg == 1):
            usage(1)
        elif (num_arg == 2):
            usage(2)
            return (0)
    return (84)
