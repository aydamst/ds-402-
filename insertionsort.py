
def insertion_sort(arr, simulation=False):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        
        arr[pos] = cursor

    return arr