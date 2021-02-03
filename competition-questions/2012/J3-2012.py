# enlarge = int(input()) 

# star = "" 
# x = "" 
# space = "" 

# for i in range(enlarge): 
#     star = star + "*" 
#     x = x + "X" 
#     space = space + " " 
    
# for i in range(enlarge): 
#     print(star+x+star)
# for i in range(enlarge): 
#     print(space+x+x) 
# for i in range (enlarge): 
#     print(star+space+star)

k = 3 
# k = int(input()) 

# for i in range(k): 
#     print('*'*k+'x'*k+'*'*k) 
# for i in range(k): 
#     print(' '*k+'x'*k+'x'*k) 
# for i in range(k): 
#     print('*'*k+' '*k+'*'*k) 

# k = int(input())

# for line in ['*x*', ' xx', '* *']:
#     line_ex = [char*k for char in line]
#     for _ in range(k):
#         print(''.join(line_ex))

# print([''.join([char*k for char in line for line in ['*x*', ' xx', '* *']]) for _ in range(k) for line in ['*x*', ' xx', '* *']])

print(''.join(''.join([char*k for char in line])) for line in ['*x*', ' xx', '* *']))