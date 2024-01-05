def counting_sort(arr):
    
    max_val = max(arr)
    
    
    count = [0] * (max_val + 1)
    
   
    for num in arr:
        count[num] += 1
  

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr





# arr = [4, 9, 5, 0, 3, 9, 8, 7, 4, 0]
# sorted_arr = counting_sort(arr)
# print(sorted_arr)


