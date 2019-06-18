from dice import D6


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError('you must provide a die_class')
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()


class Yhand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)



