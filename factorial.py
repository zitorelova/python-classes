def factorial(n):
    
    for i in range(1, n):
        n *= i

    return max(n, 1) # 0! = 1

print(factorial(5))
