def hanoi_tower(n, A, B, C):
    if n == 1:
        return [(A, C)]
    else:
        moves = hanoi_tower(n-1, A, C, B)
        moves.append((A, C))
        moves.extend(hanoi_tower(n-1, B, A, C))
        return moves
 
#A = 'A'  sutun aval
#B = 'B'  sutun dovom
#C = 'C'  sutun sevom
#n = 3    tedade mohre

#output = hanoi_tower(n, A, B, C)

#print(output)