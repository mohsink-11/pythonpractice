def BubbleSort(arr):
    n=len(arr)

    for i in range(n):
        Swap=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                Swap=True
        
        if not Swap:
            break
    return arr
print(BubbleSort([4,3,2,1]))