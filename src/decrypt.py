##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## decrypt.py
##

import os
import math
from src.constants import EXIT_FAILURE
from src.errors_man import errors
from src.disp import key_disp, decrypt_disp
from src.matrix import key_matrix, decrypt_matrix
from src.encrypt import mul_matrix

def det2(key):
    return key[0][0] * key[1][1] - key[0][1] * key[1][0]

def inv2x2(key):
    det = det2(key)
    if (det == 0):
        exit(EXIT_FAILURE)
    return [[key[1][1] / det, -key[0][1] / det],
            [-key[1][0] / det, key[0][0] / det]]

def det3(key):
    return (key[0][0] * ((key[1][1] * key[2][2]) - (key[1][2] *key[2][1]))
    - key[0][1] * ((key[1][0] * key[2][2]) - (key[1][2] * key[2][0]))
    + key[0][2] * ((key[1][0] * key[2][1]) - (key[1][1] * key[2][0])))

def inv3x3(key):
    matrix = [[0] * 3 for k in range(3)]
    det = det3(key)
    if (det == 0):
        exit(EXIT_FAILURE)
    for i in range(3):
        for j in range(3):
            adjugate = [[n for k, n in enumerate(row) if (k != i)] 
                        for m, row in enumerate(key) if (m != j)]
            d = det2(adjugate)
            sign = math.pow(-1, i + j)
            matrix[i][j] = sign * d / det
            if (matrix[i][j] == -0.0):
                matrix[i][j] = 0.0
    return matrix

def decrypt(ac, av):
    key = key_matrix(av[2])
    if (len(key) == 1):
        key[0][0] = 1 / key[0][0] 
    elif (len(key) == 2):
        key = inv2x2(key)
    elif (len(key) == 3):
        key = inv3x3(key)
    else:
        exit(errors(4, 4))
    message = decrypt_matrix(av[1], len(key))
    key_disp(key)
    result = mul_matrix(key, message)
    print()
    decrypt_disp(result)