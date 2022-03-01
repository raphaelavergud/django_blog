#!/usr/bin/env python3

from django.test import TestCase

# this is just a test file to help myself write tests
# for whenever i forget how to do it
# i don't know how to untrack it from pushing to git.
# this is only for myself really.

class AdditionTestCase(TestCase):
    def test_add(self):
        self.assertEqual(3, add(1,2))
        self.assertEqual(4, add(2,2))
        self.assertEqual(6, add(3,3))


    def test_multiply(self):
        self.assertEqual(2, multiply(1,2))

    def test_calculate_30(self):
        expected = calculate_total(2,3)
        self.assertEqual(30, expected)

    def test_calculate_40(self):
        expected = calculate_total(3,3)
        self.assertEqual(54, expected)

def calculate_total(a, b):
    answer = 0
    answer = answer + add(a, b)
    answer = answer * multiply(a, b)
    return answer

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b