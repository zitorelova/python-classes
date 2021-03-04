# Input Specification
# The first line of input contains the integer K (1 ≤ K ≤ 100 000) which is the number of integers
# (including “zero”) your boss will say. On each of the next K lines, there will either be one integer
# between 1 and 100 (inclusive), or the integer 0.

# Output Specification
# The output is one line, containing the integer which is the correct sum of the integers read, taking
# the “zero” statements into consideration. You can assume that the output will be an integer in the
# range 0 and 1 000 000 (inclusive).

K = int(input())

l = []
print(f"The stack is {l}")
for _ in range(K):
    n = int(input())
    if n: 
        l.append(n)
        print(f"{n} was pushed to the stack")
    else: 
        last_element = l[-1]
        l.pop()
        print(f"{last_element} was popped from the stack")
    print(f"The stack is {l}\n")
print(sum(l))

# this is a stack