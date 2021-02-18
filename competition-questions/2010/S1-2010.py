"""
Input Specification
The first line of input will be an integer n (0 ≤ n ≤ 10000). Each of the remaining n lines of input
will contain a computer specification. A computer specification is of the form:
• computer name (a string of less than 20 characters)
• the RAM available (an integer R with 1 ≤ R ≤ 128)
• the CPU speed (an integer S with 1 ≤ S ≤ 4000)
• the disk drive space (an integer D with 1 ≤ D ≤ 3000)
There is one space between the name, RAM, CPU speed and disk drive space on each line.

Output Specification
The output is the name of the top two preferred computers, one name per line, sorted in decreasing
order of preference. If there is a tie in the rankings, pick the computer(s) whose name(s) are
lexicographically smallest (i.e., “Apple” is smaller than “Dell”). If there is only one computer,
output that computer on one line (i.e., do not print it twice).
"""

inps = int(input()) 
computers = [] 

for i in range(inps): 
    computers.append(input().split()) 
    


totals = [] 

for i in range(len(computers)): 
    totals.append(int(computers[i][1])*2 + int(computers[i][2])*3 + int(computers[i][3])) 
    
same = [] 

pref_list = sorted(list(zip(computers, totals)), key=lambda x: (x[-1], -x[0][0]), reverse=True)
print(pref_list)
# if pref_list[0][-1] == pref_list[1][-1]:
#     pref_list_2 = pref_list[:2]
#     pref_list_2 = sorted(pref_list_2, key=lambda x: x[0][0])
#     for pref in pref_list_2:
#         print(pref[0][0])



