import random


class Samson:
    male = True

    def __init__(self, name, male=True, **kwargs):
        self.name = name
        self.male = male

        for key, value in kwargs.items():
            setattr(self, key, value)

    def pickpoket(self):
        if self.male:
            return bool(random.randint(0, 1))
        else:
            return False

    def hide(self, light_level):
        return self.male and light_level > 10