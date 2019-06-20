from dice import D6


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError('you must provide a die_class')
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()
    
    def die_val(self, value):
        dice = []
        for each in self:
            if each == value:
                dice.append(each)
        return dice

        
class Yhand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)

    @property
    def one(self):
        return self.die_value(1)

    @property
    def two(self):
        return self.die_value(2)

    @property
    def three(self):
        return self.die_value(3)

    @property
    def four(self):
        return self.die_value(4)

    @property
    def five(self):
        return self.die_value(5)

    @property
    def six(self):
        return self.die_value(6)

    @property
    def _set(self):
        return{
            1: len(self, one),
            2: len(self, two),
            3: len(self, three),
            4: len(self, four),
            5: len(self, five),
            6: len(self, six)
        }

    
