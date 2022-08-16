
from django.test import TestCase
import sys
from .utils import Update_Recursion_Limit, fibonacci


class TestRecursionLimit(TestCase):

    def test_default_recursion_limit(self):
        self.assertEqual(sys.getrecursionlimit(), 1000)

    def test_change_recursion_limit(self):
        # check the max recursion before the change
        self.assertEqual(sys.getrecursionlimit(), 1000)
        with Update_Recursion_Limit(2000):
            # check the max recursion during the change
            self.assertEqual(sys.getrecursionlimit(), 2000)
        # check the max recursion after the change
        self.assertEqual(sys.getrecursionlimit(), 1000)

class TestFibonacci(TestCase):

    def test_zeros_to_two(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_basic(self):
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(16), 987)
        self.assertEqual(fibonacci(40), 102334155)
        self.assertEqual(fibonacci(64), 10610209857723)
        self.assertEqual(fibonacci(94), 19740274219868223167)
        self.assertEqual(
            fibonacci(200), 280571172992510140037611932413038677189525)

    def test_error(self):
        with self.assertRaises(ValueError):
            fibonacci("1")
            fibonacci("-4")
            fibonacci(-4)
            fibonacci(True)
            fibonacci(40000)

