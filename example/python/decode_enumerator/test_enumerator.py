import unittest
from enumerator import solve

class WidgetTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEquals(3, solve("111"))
        self.assertEquals(4, solve("127426"))
