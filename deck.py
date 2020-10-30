#-------------------------------------------------------------------------------
# Name:        deck.py
# Purpose:     Holds Deck class that will be used to simulate a game of xing.
#
# Author:      Kejdi Domi
#
# Created:     27-07-2020
# Copyright:   (c) ASUS 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from card import *

class Deck:
    def __init__(self):
        self.content = self.populate()

    def populate(self):
        lst = []
        for j in ["hearts", 'diamonds',"spades", 'clubs']:
            for i in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
                A = Card(i,j)
                lst.append(A)
        return lst

    def shuffle(self):
        import random
        random.shuffle(self.content)

    def show_detailed(self):
        return print([(i.value,i.suit) for i in self.content])

    def show(self):
        return print([i.value for i in self.content])

