"""Problem Description
You record all of the scoring activity at a basketball game. Points are scored by a 3-point shot, 
a 2-point field goal, or a 1-point free throw.
You know the number of each of these types of scoring for the two teams: the Apples and the Bananas. Your job 
is to determine which team won, or if the game ended in a tie.

Input Specification
The first three lines of input describe the scoring of the Apples, and the next three lines 
of input describe the scoring of the Bananas. For each team, the first line contains the number of 
successful 3-point shots, the second line contains the number of successful 2-point field goals, and 
the third line contains the number of successful 1-point free throws. Each number will be an integer 
between 0 and 100, inclusive.

Output Specification
The output will be a single character. If the Apples scored more points than the Bananas, output A. 
If the Bananas scored more points than the Apples, output B. Otherwise, output T, to indicate a tie.

Sample Input 1
10 
3 
7 
8 
9 
6

Output for Sample Input 1
B

"""

def winning_score(input):
    with open(input, 'r') as f:
        lines = [int(line.rstrip()) for line in f.readlines()]
    apples = lines[:3]
    bananas = lines[3:]
    scores = [3, 2, 1]
    apples_score = 0
    bananas_score = 0
    for num_shots, shot_type in zip(apples, scores):
        points = num_shots * shot_type
        apples_score += points
    for num_shots, shot_type in zip(bananas, scores):
        points = num_shots * shot_type
        bananas_score += points
    
    if apples_score > bananas_score:
        print('A')
    elif bananas_score > apples_score:
        print('B')
    else:
        print('T')

"""
Problem Description
You and your friend have come up with a way to send messages back and forth.
Your friend can encode a message to you by writing down a positive integer N and a symbol. You
can decode that message by writing out that symbol N times in a row on one line. Given a message 
that your friend has encoded, decode it.

Input Specification
The first line of input contains L, the number of lines in the message.
The next L lines each contain one positive integer less than 80, followed by one space, followed
by a (non-space) character.

Output Specification
The output should be L lines long. Each line should contain the decoding of the corresponding line 
of the input. Specifically, if line i + 1 of the input contained N x, then line i of the output 
should contain just the character x printed N times.

"""

def decompress(input):
    with open(input, 'r') as f:
        lines = [line.rstrip() for line in f]
    for i in range(int(lines[0])):
        temp = lines[i+1].split(' ')
        print(temp[1] * int(temp[0]))


# decompress('decompress.txt')


def time_to_decompress(input):
    with open(input, 'r') as f:
        lines = [line.rstrip() for line in f]
    for i in range(int(lines[0])):
        spec = lines[i+1].split(' ')
        print(spec[1] * int(spec[0]))

"""
Problem Description
Your new cellphone plan charges you for every character you send from your phone. Since you tend to send sequences of symbols in your messages, you have come up with the following com- pression technique: for each symbol, write down the number of times it appears consecutively, followed by the symbol itself. This compression technique is called run-length encoding.
More formally, a block is a substring of identical symbols that is as long as possible. A block will be represented in compressed form as the length of the block followed by the symbol in that block. The encoding of a string is the representation of each block in the string in the order in which they appear in the string.
Given a sequence of characters, write a program to encode them in this format.
Input Specification
The first line of input contains the number N, which is the number of lines that follow. The next N lines will contain at least one and at most 80 characters, none of which are spaces.
Output Specification
Output will be N lines. Line i of the output will be the encoding of the line i + 1 of the input. The encoding of a line will be a sequence of pairs, separated by a space, where each pair is an integer (representing the number of times the character appears consecutively) followed by a space, followed by the character.

Sample Input
4
+++===!!!! 777777......TTTTTTTTTTTT (AABBC)
3.1415555

Output for Sample Input
3+3=4!
6 7 6 . 12 T 
1(2A2B1C1) 
131.11141145

"""

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

# cold_compress('compress.txt')

def flipper(input):
    state = [[1, 2], 
             [3, 4]]

    for i in range(len(input)):
        print(input[i])

    # for line in state:
    #     print(line) 

flipper('HV')