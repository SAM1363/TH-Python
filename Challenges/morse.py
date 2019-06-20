class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        result = []
        for each in self.pattern:
            if each == '.':
                result.append('dot')
            elif each == '_':
                result.append('dash')
        return '-'.join(result)

    def __iter__(self):
        yield from self.pattern

    @classmethod
    def from_string(cls, str):
        result = []
        slpit_string = str.split('-')
        for each in slpit_string:
            if each == 'dot':
                result.append('.')
            else:
                result.append('_')
        return cls(result)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

