##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## disp.py
##

import os
import math

def key_disp(matrix):
    print("Key matrix:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j < len(matrix[i]) - 1):
                print(round(matrix[i][j], 3), end = '\t')
            else:
                print(round(matrix[i][j], 3), end = '')
        print()

def mess_disp(matrix):
    print("Encrypted message:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j < len(matrix[i]) - 1):
                print(matrix[i][j], end = ' ')
            else:
                print(matrix[i][j], end = '')
        if (i < len(matrix) - 1):
            print(end = ' ')
        else:
            print()

def decrypt_disp(matrix):
    print("Decrypted message:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            c = chr(round(matrix[i][j]))
            if (c.isprintable()):
                print(c, end = '')
        if (i == len(matrix) - 1):
            print()