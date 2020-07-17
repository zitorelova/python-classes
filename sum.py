def sum(arr):
    total = 0
    for element in arr:
        total = total + element
    return total
    

def sum(arr):
    total = 0
    if len(arr) > 0:
        total = arr[0] + sum(arr[1:])
    else:
        return 0
    return total

test = [1, 2, 3, 4]

print(sum(test))