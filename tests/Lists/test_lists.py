import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src/Lists")
    )
)

from util import process_commands


class TestListOperations(unittest.TestCase):

    def test_case_1(self):
        commands = [
            "insert 0 5",
            "insert 1 10",
            "insert 0 6",
            "print",
            "remove 6",
            "append 9",
            "append 1",
            "sort",
            "print",
            "pop",
            "reverse",
            "print"
        ]

        expected = [
            [6, 5, 10],
            [1, 5, 9, 10],
            [9, 5, 1]
        ]

        self.assertEqual(process_commands(commands), expected)

    def test_case_2(self):
        commands = [
            "append 1",
            "append 2",
            "append 3",
            "print"
        ]

        expected = [
            [1, 2, 3]
        ]

        self.assertEqual(process_commands(commands), expected)

    def test_case_3(self):
        commands = [
            "append 5",
            "append 3",
            "sort",
            "print"
        ]

        expected = [
            [3, 5]
        ]

        self.assertEqual(process_commands(commands), expected)

    def test_case_4(self):
        commands = [
            "append 1",
            "append 2",
            "append 3",
            "reverse",
            "print"
        ]

        expected = [
            [3, 2, 1]
        ]

        self.assertEqual(process_commands(commands), expected)

    def test_case_5(self):
        commands = [
            "append 10",
            "append 20",
            "pop",
            "print"
        ]

        expected = [
            [10]
        ]

        self.assertEqual(process_commands(commands), expected)


if __name__ == "__main__":
    unittest.main()
