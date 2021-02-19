"""
Input Specification
The first line contains the integer N (1 ≤ N ≤ 100). The next line contains N distinct space-
separated positive integers, where each integer is at most 1 000 000.

Output Specification
Output the N integers in the unique order that Joe originally took the measurements.

Sample Input
8
10 50 40 7 3 110 90 2

Output for Sample Input
10 40 7 50 3 90 2 110

• He started measuring water levels at a low tide, his second measurement was of the water
level at high tide, and after that the measurements continued to alternate between low and
high tides.

• All high tide measurements were higher than all low tide measurements.

• Joe noticed that as time passed, the high tides only became higher and the low tides only
became lower.

"""

N = int(input())
m = [int(x) for x in input().split()]
m.sort()

# # After sorting
# # [2, 3, 7, 10, 40, 50, 90, 110]

if N % 2 == 0:
    middle = int(N/2)
else:
    middle = int((N+1)/2)
lows = m[:middle][::-1]
highs = m[middle:]

answer = []
for i in range(middle):
    try:
        answer.append(str(lows[i]))
    except:
        pass
    try:
        answer.append(str(highs[i]))
    except:
        pass

print(' '.join(answer))

# # l = [10, 40, 7, 50, 3, 90, 2, 110]
# # print(l[::-1])

# l = [1, 2, 3, 4, 5]