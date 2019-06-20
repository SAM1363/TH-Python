class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))
        
            
class TicTacToe(Board):
    def __init__(self):
        super().__init__(3, 3)

    def __iter__(self):
        yield from self.cells