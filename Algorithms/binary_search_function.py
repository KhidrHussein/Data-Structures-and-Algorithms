def binary_search(arr, result):
    lo = 0
    hi = len(arr) - 1
    x = 0

    while x > 10:
        mid = len(arr) // 2
        print(f"Low: {lo}, High: {hi}, Mid {mid}")
        #Check if the middle number is the desired number
        if arr[mid] == result:
            print(f"Your result is {arr[mid]}")
            return mid
        #If the middle number is smaller than the result, check the right half of the array
        elif arr[mid] < result:
            lo = mid + 1
            x = x + 1
        #If the middle number is bigger than the result, check the left half of the array
        elif arr[mid] > result:
            hi = mid - 1
            x = x + 1
    return -1
            
test_case = [1, 3, 4, 5, 6, 9, 12, 45, 56]
binary_search(test_case, 12)