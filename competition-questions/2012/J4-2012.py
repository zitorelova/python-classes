# Input Specification
# The input will be two lines. The first line will contain the positive integer K (K < 10), which
# is used to compute the shift value. The second line of input will be the word, which will be a
# sequence of uppercase characters of length at most 20.

# Output Specification
# The output will be the decoded word of uppercase letters.

# Sample Input 1
# 3
# FXAB

# Output for Sample Input 1
# ZOOM

# Formula 
# S = 3P + K

K = int(input())
message = input()

output = ''
for i, letter in enumerate(message):
    P = i + 1
    S = 3 * P + K
    decoded = ord(letter) - S
    if decoded < 65:
        decoded = 91 + decoded - 65
    output += chr(decoded)
print(output)


# alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# output = ''
# for i, letter in enumerate(message):
#     P = i + 1
#     S = 3 * P + K
#     letter_index = alphabet.index(letter)
#     decoded_index = letter_index - S
#     output += alphabet[decoded_index]
# print(output)
