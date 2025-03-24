import random

def start_game():
    mat=[]
    for i in range(4):
        mat.append([0] * 4)

    add_new_2(mat)
    return mat

def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    mat[r][c] = 2

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                return 'YOU WON'
            
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'NEXT'
            
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j + 1]):
                return 'NEXT'
            
    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'NEXT'
        
    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'NEXT'
    return 'YOU LOST'

def compress(mat):
    changed = False

    new_mat = []

    for i in range(4):
        new_mat.append([0] * 4)

    for i in range(4):