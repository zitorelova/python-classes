# Input Specification
# The input will be a single integer in the range 1..10.

# Output Specification
# The output is the number of ways of producing that number on two hands, subject to the rules
# outlined above.

# key = int(input())
answer = {1: 1, 2: 2, 3: 2, 4: 3, 5: 3}

# print(answer[key])

count=0 
n=int(input()) 
for l in range(0,6,1): 
    for r in range(0,6,1): 
        print("l %s r %s" % (l,r))
        if l>=r and l+r==n: 
            count=count+1 
            
print(count) 

n = int(input())

if n < 6:
    count = n // 2 + 1
else:
    left = 5
    right = n - 5
    count = 1
    for _ in range(n//2):
        left -= 1
        right += 1
        if right > left:
            break
        count += 1

print(count)