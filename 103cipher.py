#!/usr/bin/python3

##
## EPITECH PROJECT, 2020
## 102architect
## File description:
## 102architect main file
##

import os
import math
from sys import argv
from src.constants import NB_ARGS, EXIT_FAILURE
from src.errors_man import errors
from src.encrypt import encrypt
from src.decrypt import decrypt

def main(ac, av):
    if (ac == 1 or (ac == 2 and av[1] == "-h")):
        exit(errors(1, ac))
    elif (ac != NB_ARGS):
        exit(errors(2, ac))
    if (av[3] not in ["0", "1"]):
        exit(EXIT_FAILURE)
    encrypt(ac, av) if (av[3] == "0") else decrypt(ac, av)

main(len(argv), argv)