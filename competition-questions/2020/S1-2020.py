# Input Specification
# The first line contains a number 2 ≤ N ≤ 100 000, the number of observations that follow. The
# next N lines each contain an integer 0 ≤ T ≤ 1 000 000 000 indicating the time, in seconds, of
# when a measurement was made, and an integer −1 000 000 000 ≤ X ≤ 1 000 000 000 indicating
# the position, in metres, of the Street Sprinter at that time. No two lines will have the same value of
# T .
# For 7 of the 15 available marks, N ≤ 1000.

# Output Specification
# Output a single number X, such that we can conclude that Street Sprinter’s speed was at least X
# metres/second at some point in time, and such that X is as large as possible. If the correct answer
# is C, the grader will view X as correct if |X − C|/C < 10 −5 .

N = int(input())
pairs = []
speeds = []

for _ in range(N):
    time, distance = map(int, input().split())
    pairs.append((time, distance))

pairs.sort()

current, previous = 0, 0
for pair in pairs:
    time, distance = pair[0], pair[1]
    if time == 0:
        current = distance
    else:
        speed = float(abs(distance - current)) / float(time - previous)
        previous, current = time, distance
        print(speed)