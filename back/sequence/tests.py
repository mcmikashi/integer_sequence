
from django.test import TestCase
from rest_framework.test import APITestCase
from .utils import Update_Recursion_Limit, fibonacci,lucas
from django.urls import reverse
from rest_framework import status
import sys



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

class TestTestFibonacciAPi(APITestCase):

    def test_valid_data_0(self):
        """Make sure that the api return the good value"""
        url = reverse("sequence:fibonacci",kwargs={'index':0})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,{'result':0})
    
    def test_valid_data_1(self):
        """Make sure that the api return the good value"""
        url = reverse("sequence:fibonacci",kwargs={'index':40})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,{'result':102334155})
    
    def test_invalid_data_0(self):
        """Make sure that the api return 404 code status and the good value"""
        url = reverse("sequence:fibonacci",kwargs={'index':25000})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        self.assertIn("You send an invalid index.",response.data["detail"])

    def test_invalid_data_1(self):
        """Make sure that the api return 404 code status and the good value"""
        url = reverse("sequence:fibonacci",kwargs={'index':1001})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        self.assertIn("You send an invalid index.",response.data["detail"])


class TestLucasNumbers(TestCase):

    def test_zeros_to_two(self):
        self.assertEqual(lucas(0), 2)
        self.assertEqual(lucas(1), 1)
        self.assertEqual(lucas(2), 3)

    def test_basic(self):
        self.assertEqual(lucas(10), 123)
        self.assertEqual(lucas(14), 843)
        self.assertEqual(lucas(19), 9349)
        self.assertEqual(lucas(22), 39603)
        self.assertEqual(lucas(32), 4870847)
        self.assertEqual(lucas(35),  20633239)
        self.assertEqual(lucas(38),  87403803)

    def test_error(self):
        with self.assertRaises(ValueError):
            lucas("-1")
            lucas("aaaa")
            lucas(-100)
            lucas(4000)
