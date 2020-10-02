def count(arr):
    total = 0
    for _ in arr:
        total += 1
    return total

def count_recursively(arr):
    total = 0
    if arr:
        total += 1 + count_recursively(arr[1:])
    return total


test = [1, 2, 3, 4]

print(count(test))
print(count_recursively(test))
