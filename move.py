class ChessMove:
    '''
        Data structure for a move
    '''
    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to
    
    def __str__(self):
        return f"Piece moved from {self.from_} to {self.to}"