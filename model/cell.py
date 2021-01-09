class Cell:
    class CellState (Enum):
        Alive = 1
        Dead = 2

    cellState = StringProperty(choices=[c.value for c in CellState])

    def __init__(self, x, y):
        self.x = x
        self.y = y
        

