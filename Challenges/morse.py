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


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)
