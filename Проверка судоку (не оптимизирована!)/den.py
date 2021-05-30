def valid_solution(board):
    c=-1
    b1,b2,b3,b4,b5,b6,b7,b8,b9=[],[],[],[],[],[],[],[],[]
    for y in range(0,9):
        a=[]
        for x in range(0,9):
            a.append(board[x][y])
        una=list(set(a))
        if len(una)<9:
            return False
    for i in board:
        c+=1
        d=-1
        unboard = list(set(i))
        if len(unboard)<9 or 0 in i:
            return False
        for n in i:
            d+=1
            if c<3 and d<3:
                b1.append(board[c][d])
            if 2<c<6 and d<3:
                b2.append(board[c][d])
            if c>5 and d<3:
                b3.append(board[c][d])
            if c<3 and 2<d<6:
                b4.append(board[c][d])
            if 2<c<6 and 2<d<6:
                b5.append(board[c][d])
            if c>5 and 2<d<6:
                b6.append(board[c][d])
            if c<3 and d>5:
                b7.append(board[c][d])
            if 2<c<6 and d>5:
                b8.append(board[c][d])
            if c>5 and d>5:
                b9.append(board[c][d])
    b1 = list(set(b1))
    if len(b1)<9:
        return False
    b2 = list(set(b2))
    if len(b2)<9:
        return False
    b3 = list(set(b3))
    if len(b3)<9:
        return False
    b4 = list(set(b4))
    if len(b4)<9:
        return False
    b5 = list(set(b5))
    if len(b5)<9:
        return False
    b6 = list(set(b6))
    if len(b6)<9:
        return False
    b7 = list(set(b7))
    if len(b7)<9:
        return False
    b8 = list(set(b8))
    if len(b8)<9:
        return False
    b9 = list(set(b9))
    if len(b9)<9:
        return False
    return True


board=[
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

#print(valid_solution(board))
print(list(zip(*board)))