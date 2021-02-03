# Input Specification
# The input will be four positive integers, representing the depth readings. Each integer will be on
# its own line of input.

# Output Specification
# The output is one of four possibilities. If the depth readings are increasing, then the output
# should be Fish Rising. If the depth readings are decreasing, then the output should be Fish
# Diving. If the depth readings are identical, then the output should be Fish At Constant
# Depth. Otherwise, the output should be No Fish.

# a = int(input()) 
# b = int(input()) 
# c =int(input()) 
# d = int(input()) 

# if a>b>c>d: 
#     print("Fish Diving") 
# elif a<b<c<d:
#     print("Fish Rising") 
# else: 
#     print("no fish") 

# n = [int(input()) for _ in range(4)] 

# if n[0] > n[1] > n[2] > n[3]: 
#     print('Fish Diving') 
# elif n[0] < n[1] < n[2] < n[3]: 
#     print('Fish Rising') 
# elif n[0] == n[1] == n[2] == n[3]: 
#     print('Fish At Constant Depth') 
# else: 
#     print('No Fish') 

# n = [int(input()) for _ in range(4)] 

# print(n)

# print(sorted(n) == n)
# print(sorted(n, reverse=True))

s = [int(input()) for i in range(4)] 

print('c' if len(set(s)) == 1 else 'r' if s == sorted(s) else 'd\ ' if s == sorted(s,reverse=True) else 'n') 

l = [1,1,1,1]
print(set(l))