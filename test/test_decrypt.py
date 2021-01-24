##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_decrypt.py
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.matrix import *
from src.decrypt import *

class TestKeyMatrix3InvError(TestCase):
    def test_key_matrix_inv_det3_zero(self):
        test_matrix = key_matrix("hello")

        with self.assertRaises(SystemExit) as cm:
            inv3x3(test_matrix)
        self.assertEqual(cm.exception.code, 84)

class TestKeyMatrix2InvError(TestCase):
    def test_key_matrix_inv_det2_zero(self):
        test_matrix = key_matrix("a a ")

        with self.assertRaises(SystemExit) as cm:
            inv2x2(test_matrix)
        self.assertEqual(cm.exception.code, 84)

class TestKeyMatrixInv(TestCase):
    def test_key_matrix_inv2(self):
        test_key_matrix = key_matrix("hell")
        test_matrix = inv2x2(test_key_matrix)
        self.assertEqual(round(test_matrix[0][0], 3), 0.333)
        self.assertEqual(round(test_matrix[0][1], 3), -0.312)
        self.assertEqual(round(test_matrix[1][0], 3), -0.333)
        self.assertEqual(round(test_matrix[1][1], 3), 0.321)

    def test_key_matrix_inv3(self):
        test_key_matrix = key_matrix("Homer S")
        test_matrix = inv3x3(test_key_matrix)
        self.assertEqual(round(test_matrix[0][0], 3), 0.0)
        self.assertEqual(round(test_matrix[0][1], 3), 0.0)
        self.assertEqual(round(test_matrix[0][2], 3), 0.012)

        self.assertEqual(round(test_matrix[1][0], 3), -0.004)
        self.assertEqual(round(test_matrix[1][1], 3), 0.012)
        self.assertEqual(round(test_matrix[1][2], 3), -0.012)

        self.assertEqual(round(test_matrix[2][0], 3), 0.013)
        self.assertEqual(round(test_matrix[2][1], 3), -0.013)
        self.assertEqual(round(test_matrix[2][2], 3), 0.004)

class TestDecrypt1(TestCase):
    def test_full_decrypt1(self):
        ac = 4
        av = [0, "10816 10504 11232 11232 11544", "h", 1]

        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            decrypt(ac, av)
        self.assertEqual(mock_stdout.getvalue(), "Key matrix:\n0.01\n\nDecrypted message:\nhello\n")

class TestDecrypt2(TestCase):
    def test_full_decrypt2(self):
        ac = 4
        av = [0, "19885 6560 20952 6912 10767 3552", "a a ", 1]

        with self.assertRaises(SystemExit) as cm:
            decrypt(ac, av)
        self.assertEqual(cm.exception.code, 84)

class TestDecrypt3(TestCase):
    def test_full_decrypt3(self):
        ac = 4
        av = [0, "21724 21715 11232 23220 23229 11664", "hello", 1]

        with self.assertRaises(SystemExit) as cm:
            decrypt(ac, av)
        self.assertEqual(cm.exception.code, 84)

class TestDecrypt4(TestCase):
    def test_full_decrypt4(self):
        ac = 4
        av = [0, "0", "hellowwwwwwww", 1]

        with self.assertRaises(SystemExit) as cm:
            decrypt(ac, av)
        self.assertEqual(cm.exception.code, 84)