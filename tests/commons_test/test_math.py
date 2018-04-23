from unittest import TestCase, main

from commons.math import addition


class TestAddition(TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 2), 4)
