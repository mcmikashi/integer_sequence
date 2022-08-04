
from django.test import TestCase
import sys
from .utils import Update_Recursion_Limit


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
