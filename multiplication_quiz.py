#!/usr/bin/env python3
# To see how much PyInputPlus is doing for you, try re-creating the multipli-
# cation quiz project on your own without importing it.This program will
# prompt the user with 10 multiplication questions, rans, ranging from 0 × 0 to
# 9 × 9.
import random, time


numberOfQuestions = 10
correctAnswers = 0
timeout = 8

for questionNumber in range(numberOfQuestions):
    attempt = 3
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'#{questionNumber+1}: {num1} x {num2} = '
    startTime = time.time()
    endTime = startTime + timeout
    print(f'You have {timeout} seconds to answer!')
    while True:
        if time.time() < endTime:
            try:
                answer = int(input(prompt))
            except ValueError:
                print('Insert a number!')
                print(f'You have {round(endTime - time.time(), 2)} seconds left! Hurry up.')
                continue
            else:
                if answer == num1 * num2:
                    print('Correct!')
                    time.sleep(1)
                    correctAnswers += 1
                    break
                elif attempt > 1:
                    print('Try again!')
                    print(f'You have {round(endTime - time.time(), 2)} seconds left! Hurry up.')
                    attempt -= 1
                else:
                    print('Out of attempts')
                    break
        else:
            print('Out of time')
            break
print(f'Score: {correctAnswers} / {numberOfQuestions}')
