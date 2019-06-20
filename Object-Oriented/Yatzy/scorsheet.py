class Yscorsheet:
    def score_one(self, hand):
        return sum(self.one)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._set.items():
            if scores == set_size:
                scores.append(worth*set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

