input()
boards = input().split(" ")
boardLengths = [0]*2001
fences = [0]*4001

for board in boards:
    boardLengths[int(board)] += 1

for i in range(0, len(boardLengths) - 1):
    for j in range(i, len(boardLengths)):
        if i == j:
            fences[i + j] += boardLengths[i] // 2
        else:
            fences[i + j] += min(boardLengths[i], boardLengths[j])

longest, size = 0, 0

for fenceLength in fences:
    if fenceLength > longest:
        longest = fenceLength
        size = 1
    elif fenceLength == longest:
        size += 1

print(longest, size)