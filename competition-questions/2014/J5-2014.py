"""Input Specification
The input consists of three lines. The first line consists of an integer N (1 < N ≤ 30), which is
the number of students in the class. The second line contains the first names of the N students sep-
arated by single spaces. (Names contain only uppercase or lowercase letters, and no two students
have the same first name). The third line contains the same N names in some order, separated by
single spaces.
The positions of the names in the last two lines indicate the assignment of partners: the ith name
on the second line is the assigned partner of the ith name on the third line.

Output Specification
The output will be good if the two lists of names are arranged consistently, and bad if the ar-
rangement of partners is not consistent."""

# Solution 1
a = int(input()) 
b = input().split(" ") 
c = input().split(" ") 

def q(r, s, t): 
    if r % 2: 
        return "bad" 
    for i in range(len(s)):
        # s = Ada Alan Grace John
        # t = John Grace Alan Ada
        # i = 1
        # t[i] = Alan
        # s[i] = Grace
        # s.index(t[i]) = 1
        # t[s.index(t[i])] = t[1] = Grace
        if not(t[i] != s[i] and t[s.index(t[i])] == s[i]): 
            return "bad"
        return "good" 

print(q(a, b, c)) 

n = int(input()) 
first = input().split() 
second = input().split() 

i = 0 
state = "good" 
while i < n and state == "good": 
    pos = first.index(second[i]) 
    if first[i] != second[pos] or pos == i: 
        state = "bad" 
    i+=1 
    
print(state)

num_students = int(input()) 
list1 = input().split() 
list2 = input().split() 

partner_lst = [] 
for i in range(num_students): 
    pt = sorted([list1[i],list2[i]]) 
    partner_lst.append(pt) 
    num_pt = [] 
    for j in range(len(partner_lst)): 
        num_pt.append(partner_lst.count(partner_lst[j])) 
    for k in range(len(partner_lst)): 
        if num_pt[k]%2 != 0: 
            print('bad') 
            break 
        elif k==len(partner_lst)-1 and num_pt[k] % 2==0: 
            print('good') 