
def solve(board1):
    f=f_empty(board1)
    if not f:
        return True
    else:
        r,c=f
    for i in range(1,10):
        if valid(board1,i,(r,c)):
            board1[r][c]=i
            if solve(board1):
                return True
            board1[r][c]=0
    return False


def valid(board1,num,pos):

    for j in range(9):
        if num==board1[pos[0]][j] and j!=pos[1]:
            return False

    for i in range(9):
        if num==board1[i][pos[1]] and i!=pos[0]:
            return False


    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if num==board1[i][j] and (i,j)!=pos :
                return False


    return True


def f_empty(board1):
    for i in range (9) :
         for j in range (9) :
            if(board1[i][j]==0):
                return i,j

    return None

def p_board(board1):
    for i in range (9) :
        for j in range (9) :
            print(str(board1[i][j])+" ", end="")
        print("")



