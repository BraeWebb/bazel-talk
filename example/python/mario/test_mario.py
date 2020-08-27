import unittest
from mario import get_position_in_direction

class MarioTestCase(unittest.TestCase):
    def test_directions(self):
        self.assertEquals((0, 1), get_position_in_direction((0, 0), "u"))
        self.assertEquals((1, 0), get_position_in_direction((1, 1), "d"))
        self.assertEquals((0, 1), get_position_in_direction((1, 1), "l"))
        self.assertEquals((2, 1), get_position_in_direction((1, 1), "r"))


if __name__ == '__main__':
    unittest.main()
