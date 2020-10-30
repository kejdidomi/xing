# Using xing module to analyze who wins the most games in xing
import time

from xing import *

import interactive_histogram

p1_wins = 0
p2_wins = 0
draw = 0

s = time.time()
for i in range(100000):
    a = xing(2)
    if a == 1:
        p1_wins += 1
    elif a == 2:
        p2_wins += 1
    else:
        draw += 1
f = time.time()

new = interactive_histogram.Histogram([p1_wins, p2_wins, draw])
new.show(1000)
print(f-s)
