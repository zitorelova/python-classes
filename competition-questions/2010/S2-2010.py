# Input Specification
# The first line of input will be an integer k (1 ≤ k ≤ 20), representing the number of characters and
# associated codes. The next k lines each contain a single character, followed by a space, followed
# by the binary sequence (of length at most 10) representing the associated code of that character.
# You may assume that the character is an alphabet character (i.e., ‘a’...‘z’ and ‘A’..‘Z’). You may
# assume that the sequence of binary codes has the prefix-free property. On the k + 2nd line is the
# binary sequence which is to be decoded. You may assume the binary sequence contains codes
# associated with the given characters, and that the k + 2nd line contains no more than 250 binary
# digits.

# Output Specification
# On one line, output the characters that correspond to the given binary sequence.

# Sample Input
# 5
# A 00
# B 01
# C 10
# D 110
# E 111
# 00000101111

# Output for Sample Input
# AABBE

# a = int(input()) 
# decoder = [] 
# for i in range(a): 
#     decoder.append(input().split()) 

# huffmancode = (input()) 
# huffmancode = [char for char in huffmancode] 


# decoded = [] 
# end = 1

# while len(huffmancode) > 0:
#     substr = huffmancode[:end]
#     substr = ''.join(substr)
#     for i in decoder:
#         if substr == i[1]:
#             decoded.append(i[0])
#             huffmancode = huffmancode[end:]
#             end = 0
#     end += 1
# print(decoded)

# for i in range(len(decoder)): 

k = int(input())
huffman_dict = {}

for i in range(k):
    letter = input().split()
    huffman_dict[letter[1]] = letter[0]
huffman_code = input()

huffman_decoded = ''
end = 1

while len(huffman_code) > 0:
    substr = huffman_code[:end]
    if substr in huffman_dict:
        huffman_decoded += huffman_dict[substr]
        huffman_code = huffman_code[end:]
        end = 0
    end += 1

print(huffman_decoded)
