##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_encrypt.py
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.matrix import *
from src.encrypt import *

class TestMulMatrix(TestCase):
    def test_mul_matrix(self):
        test_key_matrix = key_matrix("hell")
        test_mess_matrix = mess_matrix("it's a test", len(test_key_matrix))
        test_matrix =   [[23448, 23133], [16476, 16359], [13804, 13708],
                        [15856, 15760], [22924, 22621], [12064, 11716]]
        self.assertEqual(mul_matrix(test_key_matrix, test_mess_matrix), test_matrix)

class TestEncryp1(TestCase):
    def test_full_encrypt1(self):
        ac = 4
        av = [0, "hello", "h", 1]

        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            encrypt(ac, av)
        self.assertEqual(mock_stdout.getvalue(),
            "Key matrix:\n104\n\nEncrypted message:\n10816 10504 11232 11232 11544\n")

class TestEncryp2(TestCase):
    def test_full_encrypt2(self):
        ac = 4
        av = [0, "hello", "adb", 1]

        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            encrypt(ac, av)
        self.assertEqual(mock_stdout.getvalue(),
            "Key matrix:\n97\t100\n98\t0\n\nEncrypted message:\n19986 10400 21060 10800 10767 11100\n")
