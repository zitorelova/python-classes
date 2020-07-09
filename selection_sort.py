play_count = [156, 141, 35, 94, 88, 61, 111]

def find_largest(arr):
    largest = arr[0] # set the largest value in the array
    largest_index = 0 # set the largest index in the array

    for i in range(1, len(arr)): # loop through each value in the array
        if arr[i] > largest: # if the value is larger than the value we already have in the 'largest' variable
            largest = arr[i] # replace it
            largest_index = i # replace the index

    return largest_index

def selection_sort(arr):
    new_arr = [] # create an empty array
    for i in range(len(arr)):
        largest = find_largest(arr)
        new_arr.append(arr.pop(largest))     
    return new_arr

print(selection_sort(play_count))