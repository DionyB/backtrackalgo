# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:47:52 2021

@author: shero
"""
import numpy as np 
#Backtracking algorithm

def knighttourprob(n):
    board = [[-1 for i in range(n)] for j in range(n)]
    knightourproblemhelper(n=n, board=board, x=0, y=0, counter = 0)
    
    return np.array(board)
    
def knightourproblemhelper(n,board,x,y,counter):
    if counter == n**2:
        return True
    
    if x<0 or x>=n or y<0 or y >= n or board[x][y] != -1:
        return False
    board[x][y] = counter  
    for x_new,y_new in zip([2,2,-2,-2,1,1,-1,-1],[1,-1,-1,1,2,-2,2,-2]):
        if knightourproblemhelper(n,board, x + x_new, y+ y_new, counter + 1):
            return True
    board[x][y] = -1
    return False

def issafe(n,board,x,y):
    if x<0 or y<0 or x>=n or y>=n or board[y][x] != -1:
            return False


# def knighttourprob2(n):
#     board = [[-1 for i in range(n)] for j in range(n)]
#     knighttourproblemhelper2(n=n, board=board, x=0, y=0, counter = 0)

#     print(np.array(board))

# def knighttourproblemhelper2(n,board,x,y,counter):
#     while True:
#         counter = board[x][y]
#         if counter == n**2:
#             break
#         for x_new,y_new in zip([2,2,-2,-2,1,1,-1,-1],[-1,1,1,-1,2,-2,2,-2]):
#             x = x + x_new
#             y = y + y_new
#             if issafe(n,board = board,x = x,y =y):
#                 knighttourproblemhelper2(n,board,x,y,counter + 1)
                

#Ratmazeproblem
                
                
        