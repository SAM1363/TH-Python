def yatzy_hand(self, hand):
    if len(set(hand)) == 1:
        return 50
    else:
        return 0

# set() will return a uneaqu number, so if all the number is the same,
# the length of the hand will be 1


