import random

numberOfStreaks = 0
experiment_range = 10000
streak_value = 6

for experimentNumber in range(experiment_range):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = []
    count_H, count_T = 0, 0
    for coin_flip in range(100):
        coin_flip = random.randint(0, 1)
        if coin_flip == 1:
            coin_flips.append('H')
        else:
            coin_flips.append('T')
    #print(coin_flips)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for coin_flip in coin_flips:
        if coin_flip == 'H':
            count_H += 1
            count_T = 0
        if coin_flip == 'T':
            count_T += 1
            count_H = 0
        if (count_H or count_T) == streak_value:
            numberOfStreaks += 1
            count_H, count_T = 0, 0
    #print(numberOfStreaks)
print(f'Chance of streak of {streak_value}: {(numberOfStreaks / (100 * experiment_range)) * 100}%')
