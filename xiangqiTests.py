# Author: Jessica Dutton
# Description: unit tests for Xiangqi

import unittest
from xiangqi import XiangqiGame

class TestXianqi(unittest.TestCase):
    """
    defines unit tests for Xianqi
    """
    def setup(self):
        pass

    def test1(self):
        """
        tests black putting red in check, red attempting to make a move that does not take it out of check
        """
        game = XiangqiGame()
        game.make_move("a4", "a5")
        game.make_move("b10", "c8")
        game.make_move("b3", "b5")
        game.make_move("a10", "a9")
        game.make_move("b5", "i5")
        game.make_move("h10", "i8")
        game.make_move("i5", "i8")
        game.make_move("i10", "i8")
        game.make_move("h3", "h7")
        game.make_move("a9", "d9")
        game.make_move("h7", "e7")
        game.make_move("c8", "e7")
        game.make_move("e1", "e2")
        game.make_move("d9", "d1")
        game.make_move("c1", "e3")
        game.make_move("d1", "f1")
        game.make_move("g1", "i3")
        game.make_move("c10", "e8")
        game.make_move("e2", "d2")
        game.make_move("h8", "g8")
        game.make_move("b1", "c3")
        game.make_move("f1", "a1")
        game.make_move("c3", "b1")
        game.make_move("a1", "b1")
        game.make_move("h1", "g3")
        game.make_move("b1", "i1")
        game.make_move("g3", "e2")
        game.make_move("i1", "i3")
        game.make_move("e3", "g5")
        game.make_move("i3", "f3")
        game.make_move("e2", "g3")
        game.make_move("f3", "g3")
        game.make_move("d2", "d1")
        game.make_move("g3", "g1")
        game.make_move("d1", "d2")
        game.make_move("g1", "g4")
        game.make_move("c4", "c5")
        game.make_move("g8", "g5")
        game.make_move("e4", "e5")
        game.make_move("g4", "d4")
        self.assertEqual(game.is_in_check("black"), False)
        self.assertEqual(game.is_in_check("red"), True)
        self.assertEqual(game.make_move("c5", "c6"), False)   # red attempt to move piece that would not take itself out of check

    def test2(self):
        """
        test win for black
        """
        game = XiangqiGame()
        game.make_move("b3", "b7")
        game.make_move("b10", "c8")
        game.make_move("e1", "e2")
        game.make_move("h10", "g8")
        game.make_move("c1", "e3")
        game.make_move("a10", "a9")
        game.make_move("e3", "c5")
        game.make_move("a9", "f9")
        game.make_move("b7", "e7")
        game.make_move("c8", "e7")
        game.make_move("e4", "e5")
        game.make_move("f9", "f1")
        game.make_move("e2", "d2")
        game.make_move("f1", "g1")
        game.make_move("d1", "e2")
        game.make_move("h8", "h1")
        game.make_move("i1", "h1")
        game.make_move("g1", "h1")
        game.make_move("b1", "c3")
        game.make_move("h1", "a1")
        game.make_move("c3", "a2")
        game.make_move("a1", "a2")
        game.make_move("d2", "d1")
        game.make_move("a2", "e2")
        game.make_move("h3", "a3")
        game.make_move("i10", "h10")
        game.make_move("a3", "a2")
        game.make_move("h10", "h1")
        self.assertEqual(game.get_game_state(), "BLACK_WON")
        self.assertEqual(game.make_move("a4", "a5"), False) # red attempt to move different piece after being in checkmate



