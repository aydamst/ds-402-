count = 0
def binary_search(list, item):
    global count
    low = 0
    high = int(len(list)-1)
    while low <= high:
        count+=1
        mid = int((low + high)/2 )
        guess = int(list[mid])
      
        if guess == item:
            #return mid
            return count  
        elif guess > item:
                high = mid-1
        else:
                low = mid + 1
    return None
 


#my_list = [1, 3, 5, 7, 9, 11, 13]

#print (binary_search(my_list, 9)) 
#print (binary_search(my_list, -1)) 