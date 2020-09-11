"""
Input Specification
The first line of input contains the number of drops of paint, N , where 2  N  100 and N is an
integer. Each of the next N lines contain exactly two positive integers X and Y separated by one
comma (no spaces). Each of these pairs of integers represents the coordinates of a drop of paint on
the canvas. Assume that X < 100 and Y < 100, and that there will be at least two distinct points.
The coordinates (0, 0) represent the bottom-left corner of the canvas.
For 12 of the 15 available marks, X and Y will both be two-digit integers.

Output Specification
Output two lines. Each line must contain exactly two non-negative integers separated by a single
comma (no spaces). The first line represents the coordinates of the bottom-left corner of the rect-
angular frame. The second line represents the coordinates of the top-right corner of the rectangular
frame.
"""

N = int(input())
x, y = [], []

for i in range(N):
    point = input()
    x_coor, y_coor = point.split(',')
    x.append(int(x_coor))
    y.append(int(y_coor))

print(f'{min(x) - 1},{min(y) - 1}')
print(f'{max(x) + 1},{max(y) + 1}')
