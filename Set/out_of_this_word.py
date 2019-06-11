import random

WORDS = (
    'treehouse',
    'python',
    'leaner'
)


def prompt_for_words(challenge):
    guesses = set()
    print('What word can you find in the word "{}" ?'.format(challenge))
    print('Enter "Q" to quit')
    while True:
        guess = input('{} words > '.format(guesses))
        if guesses.upper() == Q:
            break
        gusses.add(guess.lower())
    return guesses

challenge_word = random.choice(WORDS)

player1 = prompt_for_words(challenge_word)
player2 = prompt_for_words(challenge_word)


