"""
Input Specification
The first line of input contains the integer K (1 ≤ K ≤ 100). The second line of input contains
the integer m (1 ≤ m ≤ 10), which is the number of rounds of removal. The next m lines each
contain one integer. The ith of these lines (1 ≤ i ≤ m) contains r i ( 2 ≤ r i ≤ 100) indicating that
every person at a position which is multiple of r i should be removed.

Output Specification
The output is the integers assigned to friends who were not removed. One integer is printed per
line in increasing sorted order.

"""

# Solution 1
K = int(input()) 
friends = [i+1 for i in range(K)] 
rounds = int(input()) 

for i in range(rounds): 
    bad = [] 
    remove = int(input())
    for friend in range(len(friends)): 
        if ((friend+1)%remove==0):
            bad.append(friends[friend])
    for baddie in bad: 
        friends.remove(baddie) 
        
for friend in friends: 
    print(friend) 


# Solution 2
a = list(range(int(input()))) 

for j in range(int(input())): 
    b = int(input()) 
    c = list() 
    for i in range(len(a)): 
        if (i+1) % b: 
            c.append(a[i]) 
    a = c 
        
for i in a: print(i+1)     