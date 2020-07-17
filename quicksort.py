def quicksort(arr):
    if len(arr) < 2: # create the base case
        return arr # if we have 0 or 1 elements then we
                   # don't need to sort the array
    else:
        pivot = arr[0] # set the pivot equal to the 
                       # first element of the array
        less = [] # all elements less than or equal to 
                  # the pivot
        greater = [] # all elements greater than the
                     # pivot

        for element in arr[1:]: # loop starting from the 2nd element
            if element <= pivot:
                less.append(element)

        for element in arr[1:]:
            if element > pivot:
                greater.append(element)

        print(pivot)
        print(less)
        print(greater)

        return quicksort(less) + [pivot] + quicksort(greater) # combine the results and return them

test = [33, 15, 10, 7]

print(quicksort(test))