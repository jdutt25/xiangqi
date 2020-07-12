# Author: Jessica Dutton
# Description: Contains the XiangqiGame class for the python game of Xianqi. This file is where the game is played.
# Note that all directional inline comments are from perspective of Red ("up" represents towards black's side, "down" is moving closer to red's side, etc.)

import board, piece

class XiangqiGame:
    """
    contains abstract board game, Xianqi
    """

    def __init__(self):
        """"
        new game
        initializes the first turn to "Red" and game state to "Unfinished"
        initializes variables for the board and piece class
        initializes check status, checkmate status to False and color and full color to None (these values will be
        updated throughout the course of the game)

        """
        self._turn = "R"
        self._game_state = "UNFINISHED"
        self._game_board = board.Board()       # calls the Board class
        self._piece = piece.Piece(self._game_board.get_board)  # calls the Piece class, passing to it the current game board
        self._check_status = False
        self._checkmate_status = False
        self._color = None
        self._full_color = None

    def get_game_board(self):
        """
        returns game board class for game
        """
        return self._game_board

    def set_turn(self):
        """
        changes whose turn it is after a move is made
        """
        if self._turn == "R":
            self._turn = "B"
        elif self._turn == "B":
            self._turn = "R"

    def get_turn(self):
        """
        returns the R if it's Red's turn and B if Black's turn
        """
        return self._turn

    def set_game_state(self, color):
        """
        updates the game state to reflect the winning color
        """
        if color == "R":
            self._game_state = "RED_WON"
        elif color == "B":
            self._game_state = "BLACK_WON"

    def get_game_state(self):
        """
        returns game state -'UNFINISHED', 'RED_WON' or 'BLACK_WON'
        """
        return self._game_state

    def set_color(self, color):
        """
        sets the color of the piece
        """
        if color == "R":
            self._color = "R"
        elif color == "B":
            self._color = "B"

    def get_color(self):
        """
        returns the color of the piece
        """
        return self._color

    def set_full_color(self, color):
        """
        takes as a parameter "R" or "B" and returns the full color value ("red" or "black)
        """
        if color == "R":
            self._full_color = "red"
        elif color == "B":
            self._full_color = "black"

    def get_full_color(self):
        """
        returns the full color
        """
        return self._full_color

    def is_in_check(self, full_color):
        """
        takes as a parameter either 'red' or 'black' and returns True if that player is in check,
        returns False otherwise
        """
        self._game_board.gen_loc(full_color)  # locate the generals location
        gen_loc = self._game_board.get_gen_loc()    # assigns generals location to gen_loc for readability
        i1 = 0
        i2 = 0
        self._check_status = False              # resets check status to False (as this can change depending on moves)

        self._piece.set_legal_moves()           # resets legal moves list to []

        if full_color == "red":  # searches the board for pieces from the opposite player
            while i1 <= 9:
                while i2 < 8:
                    if self._game_board.get_board()[i1][i2][0][0] == "B":
                        value = self._game_board.get_board()[i1][i2]  # value of the moving piece (color/piece type)
                        piece = value[0][1]
                        color = value[0][0]
                        self._piece.check_legal_move(piece, color, i1, i2)
                        moves_list = self._piece.get_legal_moves()

                        while len(moves_list) > 0:  # check is move exists that would capture the general
                            if gen_loc[0] == moves_list[0] and gen_loc[1] == moves_list[1]:
                                self._check_status = True
                                del moves_list[0]  # remove set of indices from moves list
                                del moves_list[0]
                            else:
                                del moves_list[0]
                                del moves_list[0]
                    i2 += 1
                i1 += 1
                i2 = 0

        elif full_color == "black":  # searches the board for pieces from the opposite player
            while i1 <= 9:
                while i2 < 8:
                    if self._game_board.get_board()[i1][i2][0][0] == "R":
                        value = self._game_board.get_board()[i1][i2]  # value of the moving piece (color/piece type)
                        piece = value[0][1]
                        color = value[0][0]
                        self._piece.check_legal_move(piece, color, i1, i2)
                        moves_list = self._piece.get_legal_moves()

                        while len(moves_list) > 0:  # check is move exists that would capture the general
                            if gen_loc[0] == moves_list[0] and gen_loc[1] == moves_list[1]:
                                self._check_status = True
                                del moves_list[0]  # remove set of indices from moves list
                                del moves_list[0]
                            else:
                                del moves_list[0]
                                del moves_list[0]
                        moves_list.extend(self._piece.get_legal_moves())
                    i2 += 1
                i1 += 1
                i2 = 0

        return self._check_status

    def checkmate(self, full_color):
        """
        takes the color in check and checks if there are any moves they can make to get out of check. If not, the game
        is in checkmate and the given color has lost
        """

        legal_moves = []
        i1 = 0
        i2 = 0

        if full_color == "red":  # searches the board for pieces owned by red player
            while i1 <= 9:
                while i2 < 8:
                    if self._game_board.get_board()[i1][i2][0][0] == "R":
                        value = self._game_board.get_board()[i1][i2]  # value of the moving piece (color/piece type)
                        piece = value[0][1]
                        color = value[0][0]
                        self._piece.check_legal_move(piece, color, i1, i2)
                        moves_list = self._piece.get_legal_moves()

                        while len(moves_list) > 0:
                            replace = "  "
                            move_to = self._game_board.get_board()[moves_list[0]][moves_list[1]][0]
                            if move_to[0] != "R":   # can't capture own piece
                                self._game_board.set_board(i1, i2, moves_list[0], moves_list[1], value, replace)  # make move

                                if self.is_in_check(full_color) is False:  # player cannot put themselves in check
                                    legal_moves.extend([moves_list[0], moves_list[1]])
                                    replace = move_to  # put piece back
                                    self._game_board.set_board(moves_list[0], moves_list[1], i1, i2, value, replace)
                                    del moves_list[0]
                                    del moves_list[0]
                                else:
                                    replace = move_to  # put piece back
                                    self._game_board.set_board(moves_list[0], moves_list[1], i1, i2, value, replace)
                                    del moves_list[0]  # remove set of indices from moves list
                                    del moves_list[0]
                            else:
                                del moves_list[0]
                                del moves_list[0]
                    i2 += 1
                i1 += 1
                i2 = 0

            if len(legal_moves) == 0:       # red has no legal moves and is in checkmate
                self._checkmate_status = True
                self.set_game_state("B")

        elif full_color == "black":  # searches the board for pieces owned by black player
            while i1 <= 9:
                while i2 < 8:
                    if self._game_board.get_board()[i1][i2][0][0] == "B":
                        value = self._game_board.get_board()[i1][i2]  # value of the moving piece (color/piece type)
                        piece = value[0][1]
                        color = value[0][0]
                        self._piece.check_legal_move(piece, color, i1, i2)
                        moves_list = self._piece.get_legal_moves()

                        while len(moves_list) > 0:
                            replace = "  "
                            move_to = self._game_board.get_board()[moves_list[0]][moves_list[1]][0]
                            if move_to[0] != "B":   # can't capture own piece
                                self._game_board.set_board(i1, i2, moves_list[0], moves_list[1], value, replace)  # make move

                                if self.is_in_check(full_color) is False:  # player cannot put themselves in check
                                    legal_moves.extend([moves_list[0], moves_list[1]])
                                    replace = move_to  # put piece back
                                    self._game_board.set_board(moves_list[0], moves_list[1], i1, i2, value, replace)
                                    del moves_list[0]
                                    del moves_list[0]
                                else:
                                    replace = move_to  # put piece back
                                    self._game_board.set_board(moves_list[0], moves_list[1], i1, i2, value, replace)
                                    del moves_list[0]  # remove set of indices from moves list
                                    del moves_list[0]
                            else:
                                del moves_list[0]
                                del moves_list[0]
                    i2 += 1
                i1 += 1
                i2 = 0

            if len(legal_moves) == 0:       # black has no legal moves and is in checkmate
                self._checkmate_status = True
                self.set_game_state("R")


    def make_move(self, move_from, move_to):
        """
        If the square being moved from contains a piece belonging to the player whose turn it is and if the
        indicated move is  legal and if the game has not been won, proceeds with the move, removes any captured piece,
         updates the game state if necessary, updates whose turn it is, and returns True
         Otherwise, returns False
        """
        move_from1 = self._game_board.index1_converter(move_from)      # 1st index of move from square
        move_from2 = self._game_board.index2_converter(move_from)      # 2nd index of move from square
        value = self._game_board.get_board()[move_from1][move_from2]   # value of the moving piece (color/piece type)
        move_to1 = self._game_board.index1_converter(move_to)          # 1st index of move to square
        move_to2 = self._game_board.index2_converter(move_to)          # 2nd index of move to square
        move_to = self._game_board.get_board()[move_to1][move_to2][0]  # full value of the move to square
        piece = value[0][1]
        self.set_color(value[0][0])
        self.set_full_color(self.get_color())

        if self.get_color() == self.get_turn() and self.get_game_state() == 'UNFINISHED' and \
                self._game_board.get_board()[move_to1][move_to2][0][0] != self.get_color():
            self._piece.check_legal_move(piece, self.get_color(), move_from1, move_from2)

            while len(self._piece.get_legal_moves()) > 0:
                if move_to1 == self._piece.get_legal_moves()[0] and move_to2 == self._piece.get_legal_moves()[1]:
                    replace = "  "
                    self._game_board.set_board(move_from1, move_from2, move_to1, move_to2, value, replace) # move the piece on the board and update move from space to empty with replace
                    if self.is_in_check(self.get_full_color()) is False:  # player cannot put themselves in check
                        self.set_turn()  # next player's turn, first check to see if they're in check/checkmate
                        if self.get_full_color() == "red":
                            self.set_full_color("B")
                        elif self.get_full_color() == "black":
                            self.set_full_color("R")
                        self.is_in_check(self.get_full_color())         # check to see if the other color is in check
                        self.checkmate(self.get_full_color())         # check to see if the other color is in checkmate
                        return True
                    else:
                        print("you cannot make a move that puts yourself in check")
                        replace = move_to  # put piece back
                        self._game_board.set_board(move_to1, move_to2, move_from1, move_from2, value, replace)
                        del self._piece.get_legal_moves()[0]
                        del self._piece.get_legal_moves()[0]
                else:                                           # remove set of indices from moves list
                    del self._piece.get_legal_moves()[0]
                    del self._piece.get_legal_moves()[0]
            return False
        else:
            print("illegal move")
            return False



def main():
   game = XiangqiGame()
   game.make_move("a4", "a5")
  # game.get_game_board().print_board()
   game.make_move("b10", "c8")
   game.make_move("b3", "b5")
   game.make_move("a10", "a9")
   game.make_move("b5", "i5")
   game.make_move("h10", "i8")
   game.make_move("i5", "i8")
   game.make_move("i10", "i8")
   game.make_move("h3", "h7")
   game.get_game_board().print_board()
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
   print(game.is_in_check("red"))
  # print(game.make_move("c5", "c6")) THIS IS A PROBLEM


if __name__ == '__main__': main()