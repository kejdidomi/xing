# -------------------------------------------------------------------------------
# Name:        xing.py
# Purpose:     A simulated game of xing where 2 players play and in the end the
#              winner is decided.
#
# Author:      Kejdi Domi
#
# Created:     27-07-2020
# Copyright:   (c) ASUS 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import random

from deck import *
from field import *
from player import *



def xing(p=None):
    deck = Deck()
    deck.shuffle()

    field = Field()
    player1 = Player()
    player2 = Player()
    player2.d = 0

    def draw(n=6):
        rlist = []
        if len(deck.content) > 0:
            for i in range(n):
                rlist.append(deck.content.pop())
            return rlist
        else:
            pass

    field.c = draw(4)
    player1.hand = draw()
    player2.hand = draw()
    field.show()
    player1.show()
    player2.show()

    def throw():
        if player1.d == 1:
            p = player1
        else:
            p = player2

        if len(field.c) == 0:
            chosen = random.choice(p.hand)
            field.c.append(chosen)
            del p.hand[p.hand.index(chosen)]
            if p == player1:
                player1.d = 0
                player2.d = 1
            else:
                player1.d = 1
                player2.d = 0

        elif len(field.c) == 1:
            lst = []
            for i in p.hand:
                lst.append(i.value)
            if field.top() in lst:
                i = lst.index(field.top())
                del p.hand[i]
                field.clear()
                p.xing += 1
                print("XING!!!")
            else:
                if 'J' in lst:
                    i = lst.index('J')
                    del p.hand[i]
                    field.clear()
                else:
                    chosen = random.choice(p.hand)
                    field.c.append(chosen)
                    del p.hand[p.hand.index(chosen)]
            if p == player1:
                player1.d = 0
                player2.d = 1
            else:
                player1.d = 1
                player2.d = 0

        else:
            lst = []
            for i in p.hand:
                lst.append(i.value)
            if field.top() in lst:
                i = lst.index(field.top())
                del p.hand[i]
                field.clear()
            else:
                if 'J' in lst:
                    i = lst.index('J')
                    del p.hand[i]
                    field.clear()
                else:
                    chosen = random.choice(p.hand)
                    field.c.append(chosen)
                    del p.hand[p.hand.index(chosen)]
            if p == player1:
                player1.d = 0
                player2.d = 1
            else:
                player1.d = 1
                player2.d = 0
        field.show()
        player1.show()
        player2.show()

    def play():
        for i in range(4):
            for j in range(12):
                throw()
            player1.hand = draw()
            player2.hand = draw()
        if i == 3:
            if player1.xing > player2.xing:
                print("P1 wins with result:", player1.xing, player2.xing)
                field.winner = 1
            elif player1.xing < player2.xing:
                print("P2 wins with result:", player1.xing, player2.xing)
                field.winner = 2
            else:
                print("Draw with result:", player1.xing, player2.xing)

    # print("Enter 1 if you want to play and anything else if you do not want to.")
    if p:
        play()
        return field.winner
    else:
        return

if len(sys.argv) == 2:
    xing(int(sys.argv[1]))

# input() == 1
