#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:32:18 2021

@author: austinlanglinais
"""
def spin_words(sentence):
    temp = list(sentence.split(" "))
    for x in range(len(temp)):
        if len(temp[x]) >= 5:
            temp[x] = temp[x][::-1]
        else:
            pass        
    print (" ".join(temp))


test = "Just this dessap a of secapS or that in with be one takes"
spin_words(test)

dates 