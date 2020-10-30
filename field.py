#-------------------------------------------------------------------------------
# Name:        field.py
# Purpose:     Simulating the playing field in xing
#
# Author:      Kejdi Domi
#
# Created:     27-07-2020
# Copyright:   (c) ASUS 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Field:
    def __init__(self, winner=None):
        self.c = []
        self.winner = None

    def clear(self):
        self.c = []

    def top(self):
        return self.c[-1].value

    def show_detailed(self):
        return print([(i.value,i.suit) for i in self.c])

    def show(self):
        return print([i.value for i in self.c])