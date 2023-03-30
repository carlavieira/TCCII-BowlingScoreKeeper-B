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
        self.assertEqual(gameTest.score(), 55)


    def test_set_bonus(self):
        frames = [Frame(1,0)]*9
        frames.append(Frame(10,0))
        gameTest = BowlingGame(frames)
        self.assertEqual(len(gameTest.frames), 10)
        self.assertTrue(gameTest.is_next_frame_bonus())
        gameTest.set_bonus(2,0)
        self.assertEqual(gameTest.score(), 21)

if __name__ == '__main__':
    unittest.main()
