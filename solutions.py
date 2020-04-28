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


def flipper(input):
    state = [[1, 2],
              [3, 4]]

    def flip_horizontally(state):
        state = state[::-1]
        return state

    def flip_vertically(state):
        for ix in range(len(state)):
            state[ix] = state[ix][::-1]
        return state
    
    for flip in input:
        if flip == 'H':
            state = flip_horizontally(state)
        elif flip == 'V':
            state = flip_vertically(state)

    for line in state:
        print(line)

def rule_of_three(input):
    with open(input, 'r') as f:
        lines = [line.rstrip().split(' ') for line in f]

    def find_all(string, substring):
        start = 0
        while True:
            start = string.find(substring, start)
            if start == -1: return
            yield start
            start += 1

    def replace_at_ix(string, sub1, sub2, ix):
        return string[:ix] + string[ix:].replace(sub1, sub2, 1)

    old_states = [[lines[-1][1]]]
    new_states = []
    for step in range(int(lines[-1][0])):
        for state in old_states:
            for sub_number, (sub1, sub2) in enumerate(lines[:3]):
                indices = list(find_all(state[-1], sub1))
                for ix in indices:
                    new_seq = replace_at_ix(state[-1], sub1, sub2, ix)
                    sub_state = state.copy()
                    sub_state.extend([sub_number+1, ix+1, new_seq])
                    new_states.append(sub_state)
        old_states = new_states
        new_states = []
    solutions = [seq for seq in old_states if seq[-1] == lines[-1][-1]]
    if not solutions:
        print("No solutions found")
    else:
        print(f'There is/are {len(solutions)} possible solution/s')
        print(solutions)

def telemarketer_or_not(input):
    with open(input, 'r') as f:
        lines = [int(line.rstrip()) for line in f]
    print('ignore' if all(num in [8,9] for num in [lines[0], lines[-1]]) and lines[1] == lines[2] else 'answer')

def occupy_parking(input):
    pass






    