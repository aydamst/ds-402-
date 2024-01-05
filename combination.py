def rec_combine(n, r):
    if r == 0 or r == n:
        return 1
    if r > n:
        return 0
    return rec_combine(n - 1, r - 1) + rec_combine(n - 1, r)
    
#result = combination(6, 3)
#print("Result:", result)