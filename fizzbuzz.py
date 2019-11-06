"""
Author: Jordan Kasoff
Date: 2019

"""


def calc(end_num):
    """

    :param end_num: Passed value from terminal
    :return: FizzBuzz of list
    """
    start_num = 0
    while start_num <= end_num:
        if start_num % 3 == 0 and start_num % 5 == 0:
            print("Fizzbuzz")
            start_num = start_num + 1
        elif start_num % 3 == 0:
            print("Fizz")
            start_num = start_num + 1
        elif start_num %5 == 0:
            print("Buzz")
            start_num = start_num + 1
        else:
            print(start_num)
            start_num = start_num + 1
