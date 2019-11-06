"""
Author: Jordan Kasoff
Date: 2019
Github
"""
import sys
import math


def calc(ConstA, ConstB, ConstC):
    LeftRoot = ConstB * ConstB
    RightRoot = 4 * ConstA * ConstC
    TotalRoot = math.sqrt(LeftRoot - RightRoot)
    Denom= 2 * ConstA
    AddNom = (-1 * ConstB) + (TotalRoot)
    NegNom = (-1 * ConstB) - (TotalRoot)
    RootOne = AddNom / Denom
    RootTwo = NegNom / Denom
    print (RootOne, RootTwo)


def init():
    print("Please enter in coefficients from Standard Ax^2 + Bx + C ")
    ConstA = input("Value for Constant A: ")
    ConstB = input("Value for Constant B: ")
    ConstC = input("Value for Constant C: ")
    print ("You have entered the following values: " + ConstA, ConstB, ConstC)
    calc(int(ConstA), int(ConstB), int(ConstC))



