# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        if smallest_index != i:
            # swapping without pop and insert method
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
            # arr.insert(i, arr.pop(smallest_index)

    return arr

# selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# 0,1,2,3,4,5,6,7,8,9

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # repeat at the 0 index if there was a swap
    # need a swap counter
    # compare element to its neighbor
    sc = 1
    while sc >= 1:
        sc = 0
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # swapping without pop and insert method
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # arr.insert(i, arr.pop(i+1))
                sc += 1

    return arr

# bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# 0,1,2,3,4,5,6,7,8,9


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # get length of arr
    larr = len(arr)
    # count all elements from 0 - 9 starting at 0 each
    c_arr = [0 for x in range(10)]

    for i in arr:
        c_arr[i] += 1
    print(c_arr)

    # add neigbor(2) start from the left
    for i in range(0, larr-1):
        j = i+1
        # print(j)
        # print(c_arr[i] + c_arr[j])
        c_arr.insert(j, c_arr[i] + c_arr[j])
        print(c_arr[i] + c_arr[j])

        # c_arr.pop(j)
    for i in arr:
        n_arr = [0 for x in range(larr)]


    print(c_arr)
    return arr

# count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 7])
# 0,1,2,3,4,5,6,7,8,9

