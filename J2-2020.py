"""
Input Specification
There are three lines of input. Each line contains one positive integer. The first line contains the
value of P . The second line contains N , the number of people who have the disease on Day 0. The
third line contains the value of R. Assume that P ≤ 10 7 and N ≤ P and R ≤ 10.

Output Specification
Output the number of the first day on which the total number of people who have had the disease
is greater than P .
"""

P = int(input())
N = int(input())
R = int(input())

infected = N
people = N

days = 0
while True:
    people = people + (infected*R)
    infected = infected*R
    days += 1
    if people >= P:
        if people == P:
            print(days+1)
        else:
            print(days)
        break