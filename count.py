def count(arr):
    total = 0
    for _ in arr:
        total = total + 1
    return total

def count_recursively(arr):
    total = 0
    if arr:
        total = total + 1 + count_recursively(arr[1:])
    else:
        return total
    return total


test = [1, 2, 3, 4]

print(count(test))
print(count_recursively(test))