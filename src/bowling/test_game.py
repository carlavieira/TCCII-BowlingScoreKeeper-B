import unittest

from game import BowlingGame
from frame import Frame


class TestGames(unittest.TestCase):

    def test_add_frame_valid(self):
        gameTest = BowlingGame()
        gameTest.add_frame(Frame(1,2))
    
    def test_add_frame_invalid(self):
        gameTest = BowlingGame()
        with self.assertRaises(ValueError):
            gameTest.add_frame(Frame(-1, 0))


    def test_score(self):
        gameTest = BowlingGame([Frame(3,4), Frame(4,6), Frame(10,0), Frame(8,1)])
        self.assertEqual(gameTest.score(), 63)


    def test_set_bonus(self):
        gameTest = BowlingGame([Frame(1,0)]*9 + [10,0])
        gameTest.set_bonus(2,0)
        self.assertEqual(gameTest.score(), 63)

if __name__ == '__main__':
    unittest.main()
