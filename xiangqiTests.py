# Author: Jessica Dutton
# Description: unit tests for Xianqi

import unittest
import xiangqi, board, piece

class TestXianqi(unittest.TestCase):
    """
    defines unit tests for Xianqi
    """

    def test1(self):
        """
        tests black putting red in check, red attempting to make a move that does not take it out of check
        """
        xiangqi = xianqi()
        self.assertEqual(xiangqi.make_move("a4", "a5"), True)