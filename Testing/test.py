import unittest
import moves


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()
    def test_plus(self):
        assert 1 + 1 == 2

    def test_not_plus(self):
        assert not 3 + 4 == 8


    def test_equal(self):
        # rock1 = moves.Rock()
        # rock2 = moves.Rock()
        self.assertEqual(self.rock, moves.Rock())

    def test_not_equal(self):
        # rock = moves.Rock()
        # paper = moves.Paper()
        self.assertNotEqual(self.rock, self.paper)

    def test_rock_better_than_scissors(self):
        self.assertGreater(self.rock, self.scissors)

    def test_paper_worse_than_scissors(self):
        self.assertLess(self.paper, self.scissors)

    
if __name__ == '__main__':
    unittest.main()