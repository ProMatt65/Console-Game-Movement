from multiprocessing.connection import wait
import os
os.system('cls')
start = True
class GameGrid:
    def __init__(self, row, cur):
        self.row = row
        self.cur = cur
    
    
curItem = 3
curRow = 2
gameRow1 = ['x', 'x', 'x', 'x', 'x']
gameRow2 = ['x', 'x', 'x', '☃', 'x']
gameRow3 = ['x', 'x', 'x', 'x', 'x']
gameRow4 = ['x', 'x', 'x', 'x', 'x']
gameRow5 = ['x', 'x', 'x', 'x', 'x']


def GameDisplay():
    print(*gameRow1, sep="")
    print(*gameRow2, sep="")
    print(*gameRow3, sep="")
    print(*gameRow4, sep="")
    print(*gameRow5, sep="")


def RulesDown():
    if curRow == 1:
        gameRow1[curItem] = '☃'
    if curRow == 2:
        gameRow1[curItem] = 'x'
        gameRow2[curItem] = '☃'
    if curRow == 3:
        gameRow2[curItem] = 'x'
        gameRow3[curItem] = '☃'
    if curRow == 4:
        gameRow3[curItem] = 'x'
        gameRow4[curItem] = '☃'
    if curRow == 5:
        gameRow4[curItem] = 'x'
        gameRow5[curItem] = '☃'

def RulesUp():
    if curRow == 1:
        gameRow2[curItem] = 'x'
        gameRow1[curItem] = '☃'
    if curRow == 2:
        gameRow3[curItem] = 'x'
        gameRow2[curItem] = '☃'
    if curRow == 3:
        gameRow4[curItem] = 'x'
        gameRow3[curItem] = '☃'
    if curRow == 4:
        gameRow5[curItem] = 'x'
        gameRow4[curItem] = '☃'
    if curRow == 5:
        gameRow5[curItem] = 'x'
        gameRow5[curItem] = '☃'
        
def RulesLeft():
    if curRow == 1:
        gameRow1[curItem] = '☃'
        gameRow1[curItem + 1] = 'x'
    if curRow == 2:
        gameRow2[curItem] = '☃'
        gameRow2[curItem + 1] = 'x'
    if curRow == 3:
        gameRow3[curItem] = '☃'
        gameRow3[curItem + 1] = 'x'
    if curRow == 4:
        gameRow4[curItem] = '☃'
        gameRow4[curItem + 1] = 'x'
    if curRow == 5:
        gameRow5[curItem] = '☃'
        gameRow5[curItem + 1] = 'x'
        
def RulesRight():
    if curRow == 1:
        gameRow1[curItem] = '☃'
        gameRow1[curItem - 1] = 'x'
    if curRow == 2:
        gameRow2[curItem] = '☃'
        gameRow2[curItem - 1] = 'x'
    if curRow == 3:
        gameRow3[curItem] = '☃'
        gameRow3[curItem - 1] = 'x'
    if curRow == 4:
        gameRow4[curItem] = '☃'
        gameRow4[curItem - 1] = 'x'
    if curRow == 5:
        gameRow5[curItem] = '☃'
        gameRow5[curItem - 1] = 'x'
        
        
while start == True:
    GameDisplay()
    print("move? (up), (down), (left), (right)")
    move = input(">>")
    os.system('cls')
    if move == "left":
        curItem -= 1
        RulesLeft()
    if move == "right":
        curItem += 1
        RulesRight()
    if move == "down":
        curRow += 1
        RulesDown()
        
    if move == "up":
        curRow -= 1
        RulesUp()