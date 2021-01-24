##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_errors.py
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.errors_man import *

class TestErrors(TestCase):
    def test_usage_one(self):
        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            usage(1)
            self.assertEqual(mock_stdout.getvalue(), "Usage: ./103cipher message key flag\n")

    def test_usage_other(self):
        expected = "USAGE\n    ./103cipher message key flag\n"
        expected += "\nDESCRIPTION\n"
        expected += "    message\ta message, made of ASCII characters\n"
        expected += "    key\t\tthe encryption key, made of ASCII characters\n"
        expected += "    flag\t0 for the message to be encrypted, 1 to be decrypted\n"

        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            usage(0)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_errors(self):
        argv = ["./103cipher"]
        self.assertEqual(errors(1, len(argv)), 84)
        argv = ["./103cipher", "-h"]
        self.assertEqual(errors(1, len(argv)), 0)
        argv = ["./101pong", "message", "key", "0", "x"]
        self.assertEqual(errors(2, len(argv)), 84)