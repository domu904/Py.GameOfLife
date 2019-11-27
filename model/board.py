class Board:
    boardGrids = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def initializeGrids(self):
        for i in range(20):
            boardGrids.append(i)
