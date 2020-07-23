from quicksort import quicksort 

m = int(input())

database = []
time = -1
for i in range(m):
    line = input().split()
    letter = line[0]
    friend = int(line[1])

    if letter != "W":
        found = False
        k = 0
        while not found and k < len(database):
            if friend == database[k][0]:
                found = True
            else:
                k = k + 1

        if letter == "R":       
            if found:
                database[k][1] = time
            else:
                database.append([friend, time, 0])
        elif letter == "S":
            database[k][2] = database[k][2] + (time - database[k][1])
            database[k][1] = -1
            
    if letter == "W":
        time = time + friend - 1

    else:
        time += 1

database = quicksort(database)

for i in range(len(database)):
    if database[i][1] == -1:
        print(database[i][0], database[i][2])
    else:
        print(database[i][0], -1)