import unittest
from enumerator import solve

class EnumeratorTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEquals(3, solve("111"))
        self.assertEquals(4, solve("127426"))

    def test_edges(self):
        self.assertEquals(0, solve("0"))
        self.assertEquals(0, solve(""))
        self.assertEquals(1, solve("1"))
        self.assertEquals(2, solve("11"))
        self.assertEquals(262127, solve("1111111111111111111"))


if __name__ == '__main__':
    unittest.main()
