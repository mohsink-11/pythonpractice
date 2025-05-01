def can_be_sorted_with_one_swap(arr):
    sorted_arr = sorted(arr)
    print("Sorted Array",sorted_arr)
    mismatches = [i for i in range(len(arr)) if arr[i] != sorted_arr[i]]
    print(mismatches)

    if len(mismatches) == 0:
        return "Already sorted"  # 
    elif len(mismatches) == 2:
        i, j = mismatches
        arr[i], arr[j] = arr[j], arr[i]
        if arr == sorted_arr:
            return "Yes",arr
    return "No",arr

# Example usage
print(can_be_sorted_with_one_swap([4, 3, 2, 1]))  
