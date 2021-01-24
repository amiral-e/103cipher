##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## encrypt.py
##

import os
import math
from src.errors_man import errors
from src.disp import key_disp, mess_disp
from src.matrix import key_matrix, mess_matrix

def mul_matrix(key, message):
    result = [[0] * len(message[0]) for i in range(len(message))]

    for i in range(len(message)):
        for j in range(len(message[0])):
            for k in range(len(message[0])):
                result[i][j] += (key[k][j] * message[i][k])
    return result

def encrypt(ac, av):
    key = key_matrix(av[2])
    message = mess_matrix(av[1], len(key))
    result = mul_matrix(key, message)
    key_disp(key)
    print()
    mess_disp(result)