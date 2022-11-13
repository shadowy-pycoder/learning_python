#!/usr/bin/env python3
# Expand the stopwatch project from this chapter so that it uses the rjust()
# and ljust() string methods to “prettify” the output. (These methods were
# covered in Chapter 6.)
# Note that you will need string versions of the lapNum, lapTime, and
# totalTime integer and float variables in order to call the string methods
# on them.
# Next, use the pyperclip module introduced in Chapter 6 to copy the text
# output to the clipboard so the user can quickly paste the output to a text
# file or email.
import time
import pyperclip

lapOutputs = []
# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
# press Enter to begin
print('Started.')
startTime = time.time()
# get the first lap's start time
lastTime = startTime
lapNum = 1
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = f'{(time.time() - lastTime):.2f}'
        # initial solution
        # if lapTime[-3] != '.':  # add zero if only one digit after a floating point
        #     lapTime = lapTime + '0'
        totalTime = f'{(time.time() - startTime):.2f}'
        lapOutput = f'Lap #{str(lapNum).rjust(4)}: {totalTime.rjust(6)} ({lapTime.rjust(6)})'
        print(lapOutput, end='')
        lapOutputs.append(lapOutput)
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    result = '\n'.join(lapOutputs)
    pyperclip.copy(result)
    print('Result copied to clipboard')
