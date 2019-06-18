import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError('must have at laest 2 sides')
        if not isinstance(sides, int):
            raise ValueError('must be a number')
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __neq__(self, other):
        return int(self) != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other
        
    def __gte__(self, other):
        return int(self) > other or int(self) == other

    def __lte__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):

    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
