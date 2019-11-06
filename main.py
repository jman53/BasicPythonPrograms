import sys
import fizzbuzz
"""
Author: Jordan Kasoff
Date: 2019

"""


def main():
    print("************************************"'\n' 
          "* Welcome to Jordan's Python Suite *"'\n'
          "************************************")
    print(sys.argv)
    if sys.argv[1] == "fizzbuzz":
        if __name__ == '__main__':
            fizzbuzz.calc(int(sys.argv[2]))



main()
