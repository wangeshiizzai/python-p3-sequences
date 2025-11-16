#!/usr/bin/env python3

def print_fibonacci(length):
    # Start the Fibonacci sequence with the first two numbers
    fibonacci = [0, 1]

    # If the user wants less than 2 numbers, adjust the output
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    # Build the sequence until it reaches the desired length
    while len(fibonacci) < length:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)

    print(fibonacci)
