# Input Specification
# The input will be the 5 integers a, b, c, d, and s, each on a separate line.

# Output Specification
# The output of your program will be one of three possibilities: Nikky if Nikky is farther ahead
# after s steps are taken; Byron if Byron is farther ahead after s steps are taken; Tied if Byron and
# Nikky are at the same distance from their starting position after s steps are taken.

a, b, c, d, s = [int(input()) for x in range(5)]

nikky_steps = [1] * a + [-1] * b
byron_steps = [1] * c + [-1] * d
nikky_length = len(nikky_steps)
byron_length = len(byron_steps)
nikky_position = 0
byron_position = 0

for x in range(s):
    nikky_position += nikky_steps[x % nikky_length]
    byron_position += byron_steps[x % byron_length]

if nikky_position > byron_position:
    print('Nikky')
elif byron_position > nikky_position:
    print('Byron')
else:
    print('Tied')