# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:43:09 2023

@author: kayc2
"""

def user_selection (num):
    ans = input ("Enter Selection:")
    if ans == "q":
            return False
    return True

def main ():
    run_me = True
    while run_me:
        run_me = user_selection()