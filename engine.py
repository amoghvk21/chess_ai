from move import ChessMove

class ChessEngine:
    '''
    Stores the board and other data about the current game
    Stores the entire game state
    '''
    def __init__(self):
        self.board = [
            ["BC", "BH", "BB", "BQ", "BK", "BB", "BH", "BC"],
            ["BR", "BR", "BR", "BR", "BR", "BR", "BR", "BR"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["WC", "WH", "WB", "WQ", "WK", "WB", "WH", "WC"],
            ["WR", "WR", "WR", "WR", "WR", "WR", "WR", "WR"]
        ]
        self.whiteTurn = True
        self.moves = []
        self.notEmptySquares = set()
        self.notEmptySquares.update([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)])


    def isIllegal(self, move):
        '''
        Given a move, it decides if the move is allowed and returns true or false depending on the outcome
        '''
        pass