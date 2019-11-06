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
            if sys.argv[2] > -1
                fizzbuzz.calc(int(sys.argv[2]))
    if sys.argv[1] == "QuadForm":
        QuadForm.init()


main()
