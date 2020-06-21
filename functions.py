import random 

def createboxes(grid1):
    grid2 = [
    [[], [], []], 
    [[], [], []], 
    [[], [], []]
    ]
    for r in range(0, 9):
        row = grid1[r]
        for c in range(0,9):
            cell = grid1[r][c]
            if r < 3:
                if c < 3:
                    grid2[0][0].append(cell)
                elif c < 6:
                    grid2[0][1].append(cell)
                elif c <= 8:
                    grid2[0][2].append(cell)
            elif r < 6: 
                if c < 3:
                    grid2[1][0].append(cell)
                elif c < 6:
                    grid2[1][1].append(cell)
                elif c <= 8:
                    grid2[1][2].append(cell)
            elif r <= 8:
                if c < 3:
                    grid2[2][0].append(cell)
                elif c < 6:
                    grid2[2][1].append(cell)
                elif c <= 8:
                    grid2[2][2].append(cell)
    return grid2

def check(quest,num):
    occur = []
    for i in quest:
        if i != 0:
            occur.append(i)
    if num in occur:
        return False 
    else:
        return True      

def transverse(grid):
    result = [[],[],[],[],[],[],[],[],[]]
    for r in range(0, 9):
        row = grid[r]
        for c in range(0,9):
            cell = grid[r][c]
            if c ==0:
                result[0].append(cell)
            if c==1:
                result[1].append(cell)
            if c==2:
                result[2].append(cell)
            if c ==3:
                result[3].append(cell)
            if c==4:
                result[4].append(cell)
            if c==5:
                result[5].append(cell)
            if c ==6:
                result[6].append(cell)
            if c==7:
                result[7].append(cell)
            if c==8:
                result[8].append(cell)
    return result


def box_determine(row,column):
    for r in range(0, 9):
        for c in range(0,9):
            if row < 3:
                if column < 3:
                    return 0,0
                elif column < 6:
                    return 0,1
                elif column <= 8:
                    return 0,2
            elif row < 6: 
                if column < 3:
                    return 1,0
                elif column < 6:
                    return 1,1
                elif column <= 8:
                    return 1,2
            elif row <= 8:
                if column < 3:
                    return 2,0
                elif column < 6:
                    return 2,1
                elif column <= 8:
                    return 2,2

def search_empty(grid):
    for r in range(0,9):
        for c in range(0,9):
            cell = grid[r][c]
            if cell == 0:
                return (r,c)
    return None

def works(grid, position, num):
    num_row, num_column = position
    #check rows
    row = grid[num_row]
    if check(row,num) == False:
        return False 
    #check column
    grid2 = transverse(grid)
    column = grid2[num_column]
    if check(column,num) == False:
        return False
    #check box
    grid3 = createboxes(grid)
    box_coords = box_determine(num_row,num_column)
    box = (grid3[box_coords[0]])[box_coords[1]]
    if check(box,num) == False:
        return False 
    #Pass all 3 criteria
    return True 
        

def solve(grid):
    coord = search_empty(grid)
    if coord == None:
        return True 
    else:
        r,c = coord
        for i in range(1,10):
            if works(grid,coord,i):
                (grid[r])[c] = i
                if solve(grid):
                    return True
                (grid[r])[c] = 0
    return False  


def print_solution(grid):
    solve(grid)
    print("Solution to Sudoku Puzzle:")
    for i in range(len(grid)):
        if i == 0:
            print(' __________________________________')
        for r in range(len(grid[i])):
            num = grid[i][r]
            if r == 0:
                print('|', end='')
            print(" "+ str(num) + " ", end="")
            if (r+1) % 3 == 0:
                print(" | ", end="")
        if (i+1) % 3 == 0 and i!=8:
            print("\n|----------------------------------|")
        elif i == 8:
            print('\n|__________________________________|')
        else:
            print('\n|                                  |')

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def shuffle(s):
    return random.sample(s,len(s))

base = 3
side = base*base
rbase = range(base)
rows  = [ g*base + r for g in shuffle(rbase) for r in shuffle(rbase) ] 
cols  = [ g*base + c for g in shuffle(rbase) for c in shuffle(rbase) ]
nums  = shuffle(range(1,base*base+1))

def pattern(r,c):
    return (base*(r%base)+r//base+c)%side

def create_sudoku():
    board= [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    squares = side * side 
    empties = squares * 3//4
    for p in random.sample(range(squares), empties):
        board[p//side][p%side] = 0
    return board 

