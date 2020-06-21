import pygame
from functions import *
import time 

pygame.font.init()


class Game:
    test = create_sudoku()

    def __init__(self, rows, cols, height, width):
        self.rows = rows 
        self.cols = cols 
        self.height = height 
        self.width = width
        self.cubes = [[Cell(self.test[i][j], i, j, height, width) for j in range(cols)] for i in range(rows)]        
        self.model = None 
        self.selected = None 
    
    def grids(self, windows):
        spacing = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                strength = 3
            else:
                strength = 1 
            pygame.draw.line(windows,(0,0,0), (0,i*spacing), (self.width, i*spacing), strength)
            pygame.draw.line(windows,(0,0,0), (i*spacing,0), (i*spacing,self.height), strength)
        for r in range(self.rows):
            for c in range(self.cols):
                self.cubes[r][c].draw(window)
    
    def clicked(self,rows,cols):
        if self.selected == True:
            for r in range(self.rows):
                for c in range(self.cols):
                    self.cubes[r][c].selected == False 
        else:
            self.cubes[rows][cols].selected == True 
            self.selected = (rows,cols)
            
    def update(self):
        self.model = [[self.cubes[r][c].value for c in range(self.cols)] for r in range(self.rows)]

    def check_answer(self, answer):
        r, c = self.selected
        if self.cubes[r][c].value == 0:
            self.cubes[r][c].set(answer)
            self.update()
            if solve(self.model) and valid(self.model, answer,self.selected):
                return True 
            else:
                self.cubes[r][c].set(0)
                self.cubes[r][c].set_answer(0)
                self.update()
                return False 
    
    def click(self, position):
        if position[0] < self.width and position[1] < self.height:
            spacing = self.width / 9 #need to ensure resolution is full screen 
            x = int(position[0]//spacing)
            y = int(position[1]//spacing)
            return (x,y)
        else:
            return None 

    def sketch(self,value):
        r, c = self.selected
        self.cubes[r][c].set_answer(value)

    def delete(self):
        r, c = self.selected
        if self.cubes[r][c].value == 0:
            self.cubes[r][c].set_answer(0)

    def complete(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.cubes[r][c].value ==0:
                    return False 
        return True

class Cell:
    rows = 9
    cols = 9
    def __init__(self, value, rows, cols, height,width):
        self.rows = rows 
        self.cols = cols 
        self.height = height 
        self.width = width 
        self.value = value 
        self.selected = False 
        self.answer = 0 
        
    def draw(self, window):
        font = pygame.font.SysFont("comicsans", 40)

        spacing = self.width / 9
        x = self.cols * spacing
        y = self.rows * spacing

        if self.answer != 0 and self.value == 0:
            text = font.render(str(self.answer), 1, (128,128,128))
            window.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = font.render(str(self.value), 1, (0, 0, 0))
            window.blit(text, (x + (spacing/2 - text.get_width()/2), y + (spacing/2 - text.get_height()/2)))
    
        if self.selected:
                pygame.draw.rect(window, (255,0,0), (x,y, spacing ,spacing), 3)
        
    def set(self,value):
        self.value = value 

    def set_answer(self,value):
        self.answer= value

def redraw_window(window, board, strikes, time):
    window.fill((255,255,255))
    # Draw Strikes
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render("X " * strikes, 1, (255, 0, 0))
    window.blit(text, (20, 560))
    # Draw grid and board
    test.grids(window)
    #Draw time
    text = font.render("Time: "+format_time(time),1,(0,0,0))
    window.blit(text, (540-160,560))

def format_time(seconds):
    second = seconds%60
    minute = seconds//60
    hour = minute//60
    result = " "+str(minute)+":"+str(second)
    return result

pygame.init()
window = pygame.display.set_mode((540,600))
pygame.display.set_caption("Sudoku")
test = Game(9, 9, 540, 540)
strikes = 0
start = time.time() 
key = None 
run = True 
# Make solution available in command prompt 
print_solution(test)       
while run:
    play_time = round(time.time() - start)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
            if event.key == pygame.K_2:
                key = 2
            if event.key == pygame.K_3:
                key = 3
            if event.key == pygame.K_4:
                key = 4
            if event.key == pygame.K_5:
                key = 5
            if event.key == pygame.K_6:
                key = 6
            if event.key == pygame.K_7:
                key = 7
            if event.key == pygame.K_8:
                key = 8
            if event.key == pygame.K_9:
                key = 9
            if event.key == pygame.K_DELETE:
                test.delete()
                key = None
            if event.key == pygame.K_RETURN:
                r, c = test.selected
                if test.cubes[r][c].value == 0:
                    if test.check_answer(test.cubes[r][c].answer):
                        print("Correct!")
                    else:
                        print("Wrong!")
                        strikes += 1 
                    key = None 
                    if test.complete() or strikes==3:
                        print("Game over!")
                        run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            where = test.click(position)
            if where:
                test.clicked(where[1],where[0])
                key = None
        if test.selected and key!=None:
            test.sketch(key)
        
        redraw_window(window,test,strikes, play_time)
        pygame.display.update()

pygame.quit()

