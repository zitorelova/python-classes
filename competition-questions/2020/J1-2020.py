"""
Input Specification
There are three lines of input. Each line contains a non-negative integer less than 10. The first line
contains the number of small treats, S, the second line contains the number of medium treats, M ,
and the third line contains the number of large treats, L, that Barley receives in a day.

Output Specification
If Barley’s happiness score is 10 or greater, output happy. Otherwise, output sad.
"""

S = int(input())
M = int(input())
L = int(input())

happy = (1*S) + (2*M) + (3*L)

if happy >= 10: print("happy")
else: print("sad")