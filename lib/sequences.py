#!/usr/bin/env python3

#Write a function print_fibonacci() that prints a list of the fibonacci sequence 
#up to the length provided in the function's parameters.

def print_fibonacci(length):
    fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(fibonacci_list[0:length])

print_fibonacci(4)
    