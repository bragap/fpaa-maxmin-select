def max_min_select(arr, low, high):

    # if there is only one element
    if low == high:
        return arr[low], arr[low]
    
    # if there are two elements
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[high], arr[low]
        else:
            return arr[low], arr[high]
    
    # if there are more than two elements
    mid = (low + high) // 2
    min1, max1 = max_min_select(arr, low, mid)  # recursive call on the first half
    min2, max2 = max_min_select(arr, mid + 1, high)  # recursive call on the second half
    
    # combine the results
    final_min = min(min1, min2)
    final_max = max(max1, max2)
    
    return final_min, final_max


def find_max_min(arr):
    if len(arr) == 0:
        return "Empty array", "Empty array" # if the array is empty
    
    return max_min_select(arr, 0, len(arr) - 1)