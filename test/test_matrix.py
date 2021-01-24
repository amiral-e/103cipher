##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_matrix.py
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.matrix import *

class TestDecryptMatrix(TestCase):
    def test_decrypt_matrix(self):
        test_key_matrix = [[104, 101], [108, 108]]
        test_matrix =   [[23448, 23133], [16476, 16359], [13804, 13708],
                        [15856, 15760], [22924, 22621], [12064, 11716]]
        test_res = decrypt_matrix("23448 23133 16476 16359 13804 13708 15856 15760 22924 22621 12064 11716",
        len(test_key_matrix))
        self.assertEqual(test_res, test_matrix)

class TestKeyMatrix(TestCase):
    def test_key_matrix_2(self):
        test_matrix = [[104, 101], [108, 108]]
        self.assertEqual(key_matrix("hell"), test_matrix)

    def test_key_matrix_3(self):
        test_matrix = [[104, 101, 108], [108, 111, 0], [0, 0, 0]]
        self.assertEqual(key_matrix("hello"), test_matrix)

class TestMessMatrix(TestCase):
    def test_mess_matrix_2(self):
        test_key_matrix = [[104, 101], [108, 108]]
        test_matrix = [[84, 101], [115, 116]]
        self.assertEqual(mess_matrix("Test", len(test_key_matrix)), test_matrix)

    def test_mess_matrix_3(self):
        test_key_matrix = [[104, 101], [108, 108]]
        test_matrix = [[84, 101], [115, 116], [115, 0]]
        self.assertEqual(mess_matrix("Tests", len(test_key_matrix)), test_matrix)