def binary_search(list, item):
    low = 0
    high = len(list) - 1 # Get the length of the list

    while low <= high:
        mid = (low + high) // 2 # Divide by 2
        guess = list[mid]
        if guess == item: # Check if the number that we want is at that index
            return mid # If it is then we're done
        else:
            if item < guess: # If it is lower
                high = mid - 1 # Eliminate the upper half of our list
            else: # If it is higher
                low = mid + 1 # Eliminate the lower half of our list
    return None


sample_list = [*range(10000)]
print(sample_list)
# sample_list = [1, 3, 5, 7, 9]
# print(binary_search(sample_list, 11))
