n = int(input())
rounds = []

for i in range(n):
    line = input().split()
    for j in range(len(line)):
        rounds.append(int(line[j]))

antonia, david = 100, 100
i = 0

while i <= len(rounds) - 2:
    if rounds[i] < rounds[i+1]:
        antonia -= rounds[i+1]
    elif rounds[i] > rounds[i+1]:
        david -= rounds[i]
    i += 2

print(antonia)
print(david)