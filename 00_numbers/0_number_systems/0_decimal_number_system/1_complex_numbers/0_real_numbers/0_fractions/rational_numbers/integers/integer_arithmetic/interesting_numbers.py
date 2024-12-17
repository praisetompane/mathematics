"""
n%5 = 2
n%6 = 3

7
12
17
22
27

{multiple of 5} + 2
====================

9
15
21
27
{multiple of 6} + 3
"""

for i in range(1, 1000):
    if i % 5 == 2 and i % 6 == 3:
        print(i)
