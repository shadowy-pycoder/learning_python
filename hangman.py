from random import choice


def random_word():
    try:
        with open('sowpods.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('File not found!')
    else:
        rand_word = choice(lines).strip()
        return rand_word

if __name__ == '__main__':
    secret = random_word()
    #print(secret)
    secret = list(secret)
    clue = '_' * len(secret)
    clue = list(clue)
    guesses, bad_guesses = [], []
    max_attempt = 6
    count = len(secret)
    print(f"Guess a word: {' '.join(clue)} ({len(secret)} letters)\n")
    while max_attempt:
        if count == 0:
            print("You're the champion!")
            break
        letter = input('Guess a letter: ').upper()
        if (letter in secret) and (letter not in guesses):
            guesses.append(letter)
            for item in range(len(secret)):
                if secret[item] == letter:
                    clue[item] = letter
                    count -= 1
            print(f"\n{' '.join(clue)}\n")
        elif letter in guesses:
            print("\nYou already tried this!\n")
        elif letter in bad_guesses:
            print("\nYou already tried this!\n")
        else:
            bad_guesses.append(letter)
            max_attempt -= 1
            print("\nIncorrect!\n")
            print(f"{max_attempt} attempts left!\n")

