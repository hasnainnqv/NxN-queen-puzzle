
import numpy as np
import tkinter as tk
from PIL import ImageTk
from PIL import Image

ld = [0] * 50
rd = [0] * 50
cl = [0] * 50

class auto:
    def __init__(self) -> None:
        pass
    def printSolution(self,board):
        for row in board:
            print(row)
        print("*****************\n\n\n")



    def create_chessboard_gui(self,board,N):
        root = tk.Tk()

        img = Image.open('queen.png')
        img = img.resize((50,50))
        queenpng =  ImageTk.PhotoImage(img)
        root.title("N-Queens Puzzle")

        for i in range(N):
            for j in range(N):
                color = "white" if (i + j) % 2 == 0 else "black"
                value = queenpng if board[i][j] == 1 else ""
                label = tk.Label(root, image=value, width=10, height=3, bg=color, relief="solid")
                label.grid(row=i, column=j)

        root.mainloop()

    def solveNQUtil(self,board, col,N):
        
        if col >= N:
            return True

        for i in range(N):
            if ld[i - col + N - 1] != 1 and rd[i + col] != 1 and cl[i] != 1:
                board[i][col] = 1
                ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

                if self.solveNQUtil(board, col + 1,N):
                    return True
                board[i][col] = 0  # BACKTRACK
                ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

object = auto()
def solveNQ(i):
    N = i
    board = np.zeros((N,N),dtype=int)

    if not object.solveNQUtil(board, 0,N):
        print("Solution does not exist")
        

    object.printSolution(board)
    object.create_chessboard_gui(board,N)
for i in range(1,18):    
    A=solveNQ(i)

    ld = [0] * 50
    rd = [0] * 50
    cl = [0] * 50
