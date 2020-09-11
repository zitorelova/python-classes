"""
Input Specification
The input will consist of exactly two lines containing only uppercase letters. The first line will be
the text T , and the second line will be the string S. Each line will contain at most 1000 characters.
For 6 of the 15 available marks, S will be exactly 3 characters in length.

Output Specification
Output yes if the text, T , contains a cyclic shift of the string, S. Otherwise, output no.
"""

T = input()
S = input()
answer = "no"

for i in range(len(S)):
    if S in T:
        answer = "yes"
        break
    S = S[-1] + S[:-1]
    print(S)
print(answer)
