# Author: Jessica Dutton
# Description: Contains the Piece class and class for each pieceof the Xianqi python game


class Piece:
    """
    contains the pieces on the board and where they may legally move
    """

    def __init__(self, board):
        """
        initializes piece type to None to start, which is updated when Xiangqi make move calls Piece class and check
        legal move uses set piece type to determine and set piece type
        initializes legal move to None to start, which is updated when make move calls Piece class and checks legal move
        """
        self._piece = None
        self._legal_moves = []
        self._board = board()

    def set_piece(self, piece, color, move_from1, move_from2):
        """
        creates a piece object based on the piece that is passed to the function
        """
        if piece == "G":
            self._piece = General()
        elif piece == "A":
            self._piece = Advisor()
        elif piece == "E":
            self._piece = Elephant()
        elif piece == "H":
            self._piece = Horse()
        elif piece == "C":
            self._piece = Chariot()
        elif piece == "N":
            self._piece = Cannon()
        elif piece == "S":
            self._piece = Soldier()
        return self.get_piece

    def get_piece(self):
        """
        returns type of piece as a string (general, advisor, elphant, horse, chariot, cannon or soldier)
        """
        return self._piece

    def set_legal_moves(self):
        """
        reset the list of legal moves to an empty list
        """
        self._legal_moves = []

    def get_legal_moves(self):
        """
        returns the list of legal moves
        """
        return self._legal_moves

    def check_legal_move(self, piece, color, move_from1, move_from2):
        """
        calls set_piece to determine the type of piece, then calls the check_legal function for corresponding
        piece which returns True if the move is legal and False otherwise
        """
        self.set_piece(piece, color, move_from1, move_from2)      # passes the piece to set piece type so it's updated to appropriate object
        piece = self.get_piece()   # assigns the piece type to piece (for readablity)
        return piece.check_legal_move(color, move_from1, move_from2)

class General(Piece):
    """contains methods for general pieces"""

    def __init__(self, board):
        super().__init__(board)


    def check_legal_move(self, color, move_from1, move_from2):
        """
        may move and capture one point vertically or horizontally and may not leave the palace (with exception of
        "flying general" rule, where generals may not "see" each other)
        adds legal moves to the list get_legal_moves
        """

        if color == "R":
            if move_from1 + 1 < 10:         # one square down
                self._legal_moves.extend([move_from1 + 1, move_from2])
            if move_from1 - 1 > 6:           # one square up
                self._legal_moves.extend([move_from1 - 1, move_from2])
            if 4 <= move_from2 + 1 <= 5:    # one square right
                self._legal_moves.extend([move_from1, move_from2 + 1])
            if 3 <= move_from2 - 1 <= 4:     # one square left
                self._legal_moves.extend([move_from1, move_from2 - 1])

            while move_from1 - 1 >= 0 and self._board[move_from1 - 1][move_from2] == ["  "]:      # flying general rule
                move_from1 -= 1
            if move_from1 - 1 >= 0:
                if self._board[move_from1 - 1][move_from2] == ["BG"]:
                    self._legal_moves.extend([move_from1 - 1, move_from2])

        elif color == "B":
            if move_from1 + 1 < 3:            # one space down
                self._legal_moves.extend([move_from1 + 1, move_from2])
            if move_from1 - 1 >= 0:          # one space up
                self._legal_moves.extend([move_from1 - 1, move_from2])
            if 4 <= move_from2 + 1 <= 5:     # one space right
                self._legal_moves.extend([move_from1, move_from2 + 1])
            if 3 <= move_from2 - 1 <= 4:     # one space left
                self._legal_moves.extend([move_from1, move_from2 - 1])

            while move_from1 + 1 <= 9 and self._board[move_from1 + 1][move_from2] != ["  "]:    # flying general rule
                move_from1 += 1
            if move_from1 + 1 <= 0:
                if self._board[move_from1 + 1][move_from2] == ["RG"]:
                    self._legal_moves.extend([move_from1 + 1, move_from2])


class Advisor(Piece):
    """contains methods for advisor pieces"""

    def __init__(self):
        super().__init__()

    def check_legal_move(self, color, move_from1, move_from2):
        """
        may move one point diagonally and may not leave the palace
        adds legal moves to the list get_legal_moves
        """
        if color == "R":
            if move_from1 + 1 < 10:         # can't move out of bounds
                if move_from2 + 1 < 6:       # diagonal down and right
                    self._legal_moves.extend([move_from1 + 1, move_from2 + 1])
                if move_from2 - 1 > 2:      # diagonal down and left
                    self._legal_moves.extend([move_from1 + 1, move_from2 - 1])
            if move_from1 - 1 > 6:          # can't leave palace
                if move_from2 + 1 < 6:       # diagonal up and right
                    self._legal_moves.extend([move_from1 - 1, move_from2 + 1])
                if move_from2 - 1 > 2:      # diagonal up and left
                    self._legal_moves.extend([move_from1 - 1, move_from2 - 1])

        elif color == "B":
            if move_from1 + 1 < 3:          # can't leave palace
                if move_from2 + 1 < 6:      # diagonal down and right
                    self._legal_moves.extend([move_from1 + 1, move_from2 + 1])
                if move_from2 - 1 > 2:       # diagonal down and left
                    self._legal_moves.extend([move_from1 + 1, move_from2 - 1])
            if move_from1 - 1 >= 0:         # can't move out of bounds
                if move_from2 + 1 < 6:       # diagonal up and right
                    self._legal_moves.extend([move_from1 - 1, move_from2 + 1])
                if move_from2 - 1 > 2:      # diagonal up and left
                    self._legal_moves.extend([move_from1 - 1, move_from2 - 1])

class Elephant(Piece):
    """contains methods for elephant pieces"""

    def __init__(self):
        super().__init__()

    def check_legal_move(self, color, move_from1, move_from2):
        """"
        may move exactly two points diagonally
        may not jump over intervening pieces or cross the river
        adds legal moves to the list get_legal_moves
        """

        if color == "R":
            if move_from1 + 2 < 10:                             # can't move out of bounds
                if move_from2 - 2 >= 0 and self._board[move_from1 + 1][move_from2 - 1] == ["  "]:  # diagonal down left
                    self._legal_moves.extend([move_from1 + 2, move_from2 - 2])
                if move_from2 + 2 < 9 and self._board[move_from1 + 1][move_from2 + 1] == ["  "]:  # diagonal down right
                    self._legal_moves.extend([move_from1 + 2, move_from2 + 2])

            if move_from1 - 2 >= 5:                             # cannot cross river/out of bounds
                if move_from2 - 2 >= 0 and self._board[move_from1 - 1][move_from2 - 1] == ["  "]:    # diagonal up left
                    self._legal_moves.extend([move_from1 - 2, move_from2 - 2])
                if move_from2 + 2 < 9 and self._board[move_from1 - 1][move_from2 + 1] == ["  "]:    # diagonal up right
                    self._legal_moves.extend([move_from1 - 2, move_from2 + 2])

        elif color == "B":
            if move_from1 + 2 < 5:  # can't move out of bounds
                if move_from2 - 2 >= 0 and self._board[move_from1 + 1][move_from2 - 1] == ["  "]:  # diag down left
                    self._legal_moves.extend([move_from1 + 2, move_from2 - 2])
                if move_from2 + 2 < 9 and self._board[move_from1 + 1][move_from2 + 1] == ["  "]:
                    self._legal_moves.extend([move_from1 + 2, move_from2 + 2])                 # diagonal down right

            if move_from1 - 2 >= 0:  # cannot cross river/out of bounds
                if move_from2 - 2 >= 0 and self._board[move_from1 - 1][move_from2 - 1] == ["  "]:  # diag up left
                    self._legal_moves.extend([move_from1 - 2, move_from2 - 2])
                if move_from2 + 2 < 9 and self._board[move_from1 - 1][move_from2 + 1] == ["  "]:  # diag up right
                    self._legal_moves.extend([move_from1 - 2, move_from1 + 2])

class Horse(Piece):
    """contains methods for horse pieces"""

    def __init__(self):
        super().__init__()

    def check_legal_move(self, color, move_from1, move_from2):
        """
        may move one point vertically or horizontally and then one point diagonally away from its former position
        the horse does not jump - if there were a piece lying on a point one point away horizontally or vertically from
        the horse, then the horse's path of movement is blocked and it is unable to move in that direction
        adds legal moves to the list get_legal_moves
        """

        if move_from1 - 1 >= 0:
            if self._board[move_from1 - 1][move_from2] == ["  "] and move_from1 - 2 >= 0:  # upward moves
                self._legal_moves.extend([move_from1 - 2, move_from2 + 1])
                if move_from2 - 1 >= 0:
                    self._legal_moves.extend([move_from1 - 2, move_from2 - 1])

        if move_from1 + 2 <= 9:
            if self._board[move_from1 + 1][move_from2] == ["  "] and move_from2 + 1 <= 8:   # downward moves
                self._legal_moves.extend([move_from1 + 2, move_from2 + 1])
            if move_from2 - 1 >= 0:
                self._legal_moves.extend([move_from1 + 2, move_from2 - 1])

        if move_from2 + 1 <= 8 and self._board[move_from1][move_from2 + 1] == ["  "]:  # horizontal right moves
            if move_from1 + 1 <= 9 and move_from2 + 2 <= 8:
                self._legal_moves.extend([move_from1 + 1, move_from2 + 2])
            if move_from1 - 1 >= 0 and move_from2 + 2 <= 8:
                self._legal_moves.extend([move_from1 - 1, move_from2 + 2])

        if move_from2 - 1 >= 0:
            if self._board[move_from1][move_from2 - 1] == ["  "]:       # horizontal left moves
                if move_from1 - 1 >= 0 and move_from2 - 2 >= 0:
                    self._legal_moves.extend([move_from1 - 1, move_from2 - 2])
                if move_from1 + 1 <= 9 and move_from2 - 2 >= 0:
                    self._legal_moves.extend([move_from1 + 1, move_from2 - 2])

class Chariot(Piece):
    """contains methods for chariot pieces"""

    def __init__(self):
        super().__init__()

    def check_legal_move(color, move_from1, move_from2):
        """
        moves and captures vertically and horizontally any distance
        may not jump over intervening pieces
        adds legal moves to the list get_legal_moves
        """

        move_from1_reset = move_from1  # holds value of move_from1
        move_from2_reset = move_from2  # holds value of move_from2

        while move_from1 + 1 <= 9 and self._board[move_from1 + 1][move_from2] == ["  "]:  # moves vertical downward
            self._legal_moves.extend([move_from1 + 1, move_from2])
            move_from1 += 1
        if move_from1 + 1 <= 9 and self._board[move_from1 + 1][move_from2] != ["  "]:   # may capture one piece
            self._legal_moves.extend([move_from1 + 1, move_from2])

        move_from1 = move_from1_reset

        while move_from1 - 1 >= 0 and self._board[move_from1 - 1][move_from2] == ["  "]:  # moves vertical upward
            self._legal_moves.extend([move_from1 - 1, move_from2])
            move_from1 -= 1
        if move_from1 - 1 >= 0 and self._board[move_from1 - 1][move_from2] != ["  "]:   # may capture one piece
            self._legal_moves.extend([move_from1 - 1, move_from2])

        move_from1 = move_from1_reset

        while move_from2 + 1 <= 8 and self._board[move_from1][move_from2 + 1] == ["  "]:  # moves horizontal right
            self._legal_moves.extend([move_from1, move_from2 + 1])
            move_from2 += 1
        if move_from2 + 1 <= 8 and self._board[move_from1][move_from2 + 1] != ["  "]:  # may capture one piece
            self._legal_moves.extend([move_from1, move_from2 + 1])

        move_from2 = move_from2_reset

        while move_from2 - 1 >= 0 and self._board[move_from1][move_from2 - 1] == ["  "]:  # moves horizontal left
            self._legal_moves.extend([move_from1, move_from2 - 1])
            move_from2 -= 1
        if move_from2 - 1 >= 0 and self._board[move_from1][move_from2 - 1] != ["  "]:  # may capture one piece
            self._legal_moves.extend([move_from1, move_from2 - 1])

class Cannon(Piece):
    """contains methods for cannon pieces"""
    def __init__(self):
        super().__init__()

    def check_legal_move(self, color, move_from1, move_from2):
        """
        Cannons move like the chariots, horizontally and vertically, but capture by jumping exactly one piece
        (whether it is friendly or enemy) over to its target.
        When capturing, the cannon is moved to the point of the captured piece.
        Any number of unoccupied spaces may exist between the cannon and the cannon platform, or between
        the cannon platform and the piece to be captured, including no spaces (the pieces being adjacent) in both cases
        adds legal moves to the list get_legal_moves
        """
        jumps = 0                       # jumps increases when the piece runs into another piece
        jumps_reset = jumps
        move_from1_reset = move_from1  # holds value of move_from1
        move_from2_reset = move_from2  # holds value of move_from2

        while move_from1 + 1 <= 9 and jumps <= 1:
            if self._board[move_from1 + 1][move_from2] != ["  "]:  # moves vertical downward
                jumps += 1
                move_from1 += 1
            else:
                if jumps == 0:
                    self._legal_moves.extend([move_from1 + 1, move_from2])
                move_from1 += 1
        if move_from1 <= 9 and self._board[move_from1][move_from2] != ["  "] and jumps == 2:  # may capture one piece
            self._legal_moves.extend([move_from1, move_from2])

        move_from1 = move_from1_reset
        jumps = jumps_reset

        while move_from1 - 1 >= 0 and jumps <= 1:
            if self._board[move_from1 - 1][move_from2] != ["  "]:  # moves vertical upward
                jumps += 1
                move_from1 -= 1
            else:
                if jumps == 0:
                    self._legal_moves.extend([move_from1 - 1, move_from2])
                move_from1 -= 1

        if move_from1 >= 0 and self._board[move_from1][move_from2] != ["  "] and jumps == 2:   # may capture one piece
            self._legal_moves.extend([move_from1, move_from2])


        move_from1 = move_from1_reset
        jumps = jumps_reset

        while move_from2 + 1 <= 8 and jumps <= 1:
            if self._board[move_from1][move_from2 + 1] != ["  "]:  # moves horizontal right
                jumps += 1
                move_from2 += 1
            else:
                if jumps == 0:
                    self._legal_moves.extend([move_from1, move_from2 + 1])
                move_from2 += 1
        if move_from2 <= 8 and self._board[move_from1][move_from2] != ["  "] and jumps == 2:  # may capture one piece
            self._legal_moves.extend([move_from1, move_from2])

        move_from2 = move_from2_reset
        jumps = jumps_reset

        while move_from2 - 1 >= 0 and jumps <= 1:
            if self._board[move_from1][move_from2 - 1] != ["  "]:  # moves horizontal left
                jumps += 1
                move_from2 -= 1
            else:
                if jumps == 0:
                    self._legal_moves.extend([move_from1, move_from2 - 1])
                move_from2 -= 1
        if move_from2 >= 0 and self._board[move_from1][move_from2] != ["  "] and jumps == 2:  # may capture one piece
            self._legal_moves.extend([move_from1, move_from2])

class Soldier(Piece):
    """contains methods for soldier pieces"""
    def __init__(self):
        super().__init__()

    def check_legal_move(self, color, move_from1, move_from2):
        """
        May move and capture by advancing one point
        Once a soldier has crossed the river, they may also move (and capture) one point horizontally.
        Cannot move backward, and therefore cannot retreat; however, they may still move sideways at the enemy's edge.
        adds legal moves to the list get_legal_moves
        """

        def __init__(self):
            super().__init__()

        if color == "R":
            if move_from1 - 1 >= 0:
                self._legal_moves.extend([move_from1 - 1, move_from2])
            if move_from1 <= 4 and move_from2 + 1 <= 8:  # has crossed river, may move horizontal as well
                self._legal_moves.extend([move_from1, move_from2 + 1])
            if move_from1 <= 4 and move_from2 - 1 >= 0:
                self._legal_moves.extend([move_from1, move_from2 - 1])

        if color == "B":
            if move_from1 + 1 <= 9:
                self._legal_moves.extend([move_from1 + 1, move_from2])
            if move_from1 > 4 and move_from2 + 1 <= 8:  # has crossed river, may move horizontal as well
                self._legal_moves.extend([move_from1, move_from2 + 1])
            if move_from1 > 4 and move_from2 - 1 >= 0:
                self._legal_moves.extend([move_from1, move_from2 - 1])
