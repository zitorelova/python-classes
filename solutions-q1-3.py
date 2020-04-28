def winning_score(input):
    with open(input, 'r') as f:
        lines = [int(line.strip()) for line in f]
    apples, bananas = lines[:len(lines)//2], lines[len(lines)//2:]
    points = [3, 2, 1] 
    apples_score = sum([i*j for i, j in zip(apples, points)])
    bananas_score = sum([i*j for i, j in zip(bananas, points)])
    print('A' if apples_score > bananas_score else 'B' if bananas_score > apples_score else 'T')


def time_to_decompress(input):
    with open(input, 'r') as f:
        lines = [line.rstrip() for line in f]
    for i in range(int(lines[0])):
        spec = lines[i+1].split(' ')
        print(spec[1] * int(spec[0]))


def cold_compress(input):
    with open(input, 'r') as f:
        lines = [line.rstrip() for line in f]
    for i in range(int(lines[0])):
        line = lines[i+1]
        count = 1
        out = ''
        for j in range(len(line) - 1):
            if line[j] == line[j+1]: 
                count+=1
            else:
                out = out + str(count) + ' ' + line[j] + ' '
                count = 1
        out = out + str(count) + ' ' + line[-1]
        print(out)
