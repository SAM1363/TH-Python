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
        if guess.upper() == 'Q':
            break
        guesses.add(guess.lower())
    return guesses


def output_results(results):
    for each in results:
        print('*' + each)


challenge_word = random.choice(WORDS)

player1_words = prompt_for_words(challenge_word)
player2_words = prompt_for_words(challenge_word)

print('player1 result: ')
player1_unique = player1_words - player2_words
print('there are {} guesses, {} unique'.format(len(player1_words), len(player1_unique)))
print('-' * 10)
output_results(player1_unique)

print('player2 result: ')
player2_unique = player2_words - player1_words
print('there are {} guesses, {} unique'.format(len(player2_words), len(player2_unique)))
output_results(player2_unique)

print('shared guesses:')
shared_words = player1_words & player2_words
output_results(shared_words)