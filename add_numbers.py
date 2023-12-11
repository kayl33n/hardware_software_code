# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:53:19 2023

@author: kayc2
"""

def main () :
    print ("This program adds two numbers.")

    number1 = input("Enter the first number")
    number2 = input("Enter the second number")

    total = int(number1) + int(number2)
    print ("The total is" + str(total) + ".")
    
if __name__ == "__main__":
        main()