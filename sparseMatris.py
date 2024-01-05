def generate_complement_matrix(matrix):
    n = len(matrix)
    complement_matrix = []
    
    for i in range(n):
        row = []
        for j in range(n):
            if matrix[i][j] == 0:
                row.append(1)
            else:
                row.append(0)
        complement_matrix.append(row)
    
    return complement_matrix

     
#matrix = [[1, 0, 1], [0, 1, 0], [1, 1, 0]]
#complement = generate_complement_matrix(matrix)


#print("ماتریس اصلی:")
#for row in matrix:
#    print(row)


#print("ماتریس خلوت:")
#for row in complement:
#    print(row)