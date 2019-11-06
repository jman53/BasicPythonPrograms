import sys
import fizzbuzz
import QuadForm
"""
Author: Jordan Kasoff
Date: 2019
Github
"""


def main():
    print("************************************"'\n' 
          "* Welcome to Jordan's Python Suite *"'\n'
          "************************************")
    print(sys.argv)
    if sys.argv[1] == "fizzbuzz" or sys.argv[1] == "FIZZBUZZ":
            fizzbuzz.calc(int(sys.argv[2]))
    if sys.argv[1] == "QuadForm":
        if __name__ == '__main__':
            QuadForm.init()


main()
