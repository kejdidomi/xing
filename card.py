#-------------------------------------------------------------------------------
# Name:        card.py
# Purpose:     Object representing a card in a card game.
#
# Author:      Kejdi Domi
#
# Created:     27-07-2020
# Copyright:   (c) ASUS 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class CardValueError(Exception):
    def __init__(self,message):
        self.message = message

class CardSuitError(Exception):
    def __init__(self,message):
        self.message = message

class Card:

    def __init__(self, value, suit):
        try:
            self.value = value
            self.suit = suit

            if self.value not in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
                raise CardValueError("Invalid Value, a value can be 'A',2,3,4,5,6,7,8,9,10,'J','Q''K'")
            if self.suit not in ["hearts","spades", 'diamonds', 'clubs']:
                raise CardSuitError('Invalid Suit, suits can be "hearts","spades", "diamonds", "clubs"')

        except (CardValueError, CardSuitError) as e:
            print(e.message)



