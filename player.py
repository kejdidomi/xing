#-------------------------------------------------------------------------------
# Name:        player.py
# Purpose:     Simulating a player in xing
#
# Author:      Kejdi Domi
#
# Created:     27-07-2020
# Copyright:   (c) ASUS 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Player:
    def __init__(self):
        self.d = 1
        self.xing = 0
        self.hand = []

    def show_detailed(self):
        return print([(i.value,i.suit) for i in self.hand])

    def show(self):
        return print([i.value for i in self.hand])