# Input Specification
# The first line of input contains the number N (2 ≤ N ≤ 100). The next N lines each contain
# N positive integers, each of which is at most 10 9 . It is guaranteed that the input grid represents a
# rotated version of Barbara’s grid.

# Output Specification
# Output Barbara’s original data, consisting of N lines, each of which contain N positive integers.

N = int(input())
grid = []

for i in range(N):
    row_input = [int(i) for i in input().split()]
    grid.append(row_input)

smallest = None
min_row = 0
min_col = 0

for row_number, row in enumerate(grid):
    temp_min = min(row)
    if smallest is None or temp_min < smallest: 
        smallest = temp_min
        min_row = row_number
        min_col = row.index(smallest)

print(smallest)
print(min_row)
print(min_col)