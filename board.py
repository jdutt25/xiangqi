# Author: Jessica Dutton
# Description: Contains the Board class of the Xianqi python game

class Board:
    """"
    contains the board for the game
    """
    def __init__(self):
        """
        initializes a new board
                   Piece Key:
        BG/RG: black general/red general
        BA/RA: black advisor/red advisor
        BE/RE: black elephant/red elephant
        BH/RH: black horse/red horse
        BC/RC: black chariot/red chariot
        BN/RN: black cannon/red cannon
        BS/RS: black soldier/red soldier
        """
        self._board = [[["BC"], ["BH"], ["BE"], ["BA"], ["BG"], ["BA"], ["BE"], ["BH"], ["BC"]],
                       [["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "]],
                       [["  "], ["BN"], ["  "], ["  "], ["  "], ["  "], ["  "], ["BN"], ["  "]],
                       [["BS"], ["  "], ["BS"], ["  "], ["BS"], ["  "], ["BS"], ["  "], ["BS"]],
                       [["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "]],
                       [["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "]],
                       [["RS"], ["  "], ["RS"], ["  "], ["RS"], ["  "], ["RS"], ["  "], ["RS"]],
                       [["  "], ["RN"], ["  "], ["  "], ["  "], ["  "], ["  "], ["RN"], ["  "]],
                       [["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "]],
                       [["RC"], ["RH"], ["RE"], ["RA"], ["RG"], ["RA"], ["RE"], ["RH"], ["RC"]]]
        self._gen_loc = None

    def print_board(self):
        """
        prints the game board
        """
        print("----a-------b-------c-------d-------e------f--------g------h-------i--")
        print(self._board[0], "10")
        print("   |        |       |      |    \   |  /    |       |      |       |")
        print(self._board[1], "9")
        print("   |        |       |      |    /   |  \   |        |      |       |")
        print(self._board[2], "8")
        print("   |        |       |       |       |      |        |      |       |")
        print(self._board[3], "7")
        print("   |        |       |       |       |      |        |      |       |")
        print(self._board[4], "6")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RIVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self._board[5], "5")
        print("   |        |       |       |       |      |       |       |       |")
        print(self._board[6], "4")
        print("   |        |       |       |       |      |       |       |       |")
        print(self._board[7], "3")
        print("   |        |       |       |    \  |  /   |       |       |       |")
        print(self._board[8], "2")
        print("   |        |       |       |    /  |  \   |       |       |       |")
        print(self._board[9], "1")
        print("----a-------b-------c-------d-------e------f--------g------h-------i--")

    def set_board(self, move_from1, move_from2, move_to1, move_to2, value, replace):
        """
        updates the board, taking the first and second indices of where the piece is moving from and the first and
        second indices of where the piece is moving to, the value of the moving piece and the value that the former
        square will be replaced with (usually "  ")
        """
        self._board[move_to1][move_to2] = value         # place full value of moving piece to "move to" square
        self._board[move_from1][move_from2] = [replace]    # move from square is now empty

    def get_board(self):
        """
        returns the game board
        """
        return self._board

    def gen_loc(self, full_color):
        """
        takes "red" or "black" as a parameter and sets the location of the general for the given color
        """
        i1 = 0
        i2 = 0

        if full_color == "red":  # searches the board for red general and updates gen_loc to the indexes
            while i1 <= 9:
                while i2 < 8:
                    if self.get_board()[i1][i2][0][0] == "R" and \
                            self.get_board()[i1][i2][0][1] == "G":
                        self._gen_loc = [i1, i2]
                    i2 += 1
                i1 += 1
                i2 = 0

        elif full_color == "black":  # searches the board for red general and updates gen_loc to the indexes
            while i1 <= 9:
                while i2 < 8:
                    if self.get_board()[i1][i2][0][0] == "B" and \
                            self.get_board()[i1][i2][0][1] == "G":
                        self._gen_loc = [i1, i2]
                    i2 += 1
                i1 += 1
                i2 = 0

        return self._gen_loc

    def get_gen_loc(self):
        """"
        returns the current coordinates (indices) of the generals location (based on the color that was passed to
        gen_loc)
        """
        return self._gen_loc

    def index1_converter(self, square):
        """
        converts the given square on board to index so the list of lists that is the board may be updated
        index1 is the first index, index2 is the 2nd index
        """
        index1 = None
        row = 10  # start at top of the row and increment down
        new_val = 0  # new val is the one that will be assigned to index1 when the value of the index is equal to i

        while index1 is None:
            if len(square) == 3:  # row must be 10
                index1 = 0
            elif int(square[1]) == row:
                index1 = new_val
            else:
                row -= 1
                new_val += 1

        return index1

    def index2_converter(self, square):
        index2 = None

        while index2 is None:
            if square[0] == "a":
                index2 = 0
            elif square[0] == "b":
                index2 = 1
            elif square[0] == "c":
                index2 = 2
            elif square[0] == "d":
                index2 = 3
            elif square[0] == "e":
                index2 = 4
            elif square[0] == "f":
                index2 = 5
            elif square[0] == "g":
                index2 = 6
            elif square[0] == "h":
                index2 = 7
            else:
                index2 = 8

        return index2
