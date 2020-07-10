def fibonacci(n):
    n1, n2 = 0, 1
    print(f'Our value for n1 is {n1} and our value for n2 is {n2}')
    count = 0

    if n == 0:
        return n1
    elif n == 1:
        return n1
    else:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            print(f'Our value for n1 is {n1} and our value for n2 is {n2}')
            count += 1

fibonacci(5)



