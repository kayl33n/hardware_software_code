# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:57:59 2023

@author: kayc2
"""
def meal_test (answer): 
        if answer == 1:
            print("Fried Chicken Yummy!")
        elif answer == 2:      
            print("Burger Yummy!")
        elif answer == 3:      
            print("Pizza Yummy!")
        elif answer == 4:
            print("Tostadas, muy bien!")
        else:
            print ("That is not an option!")
    
def main ():
    print ("Which is your favorite meal?")
    print ("1.Chicken")
    print ("2. Burger")
    print ("3. Pizza")
    print ("4. Tostadas")
    answer = int(input())
    meal_test (answer)
    
if __name__ == "__main__":
    main ()