import tkinter as tk
import numpy as np
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

class NqueenGame:
    def __init__(self,N,root1,frame2):
        
        self.stack = []
        self.cond = 0 
        self.game = MainGame(N)
        self.frame2 = frame2
        self.N = N
        self.frame3 = root1
        img = Image.open("queen.png")
        img = img.resize((100,100))
        self.queenpng =  ImageTk.PhotoImage(img)

        self.board = np.zeros((self.N,self.N),dtype=int)
    

    def check_legal(self,row,col):
        self.para = [row,col]
        for i in range(self.N):
            if self.board[row][i] ==1  or self.board[i][col] ==1:
                return False
            if 0 <= row + i < self.N and 0 <= col + i < self.N and self.board[row + i][col + i] == 1:
                return False
            if 0 <= row - i < self.N and 0 <= col + i < self.N and self.board[row - i][col + i] == 1:
                return False
            if 0 <= row + i < self.N and 0 <= col - i < self.N and self.board[row + i][col - i] == 1:
                return False
            if 0 <= row - i < self.N and 0 <= col - i < self.N and self.board[row - i][col - i] == 1:
                return False
        return True


    def change_color(self,row, col):
        current_queen = buttons[row][col].cget('image')
        var = 0
        
        
        if self.cond == 1:
                pass
        elif current_queen == '':
            if self.check_legal(row,col):
                var = 1
                buttons[row][col].config(image=self.queenpng)
                buttons[row][col].config(width=105)
                buttons[row][col].config(height=95)
                self.stack.append([row,col])
                print(self.stack)
                # buttons[row][col].config(bg='black' if current_color is 'black' else 'white')
                current_queen= ''
                self.board[row][col]=var
                if np.count_nonzero(self.board == 1) == self.N:
                    messagebox.showinfo("Great ","Congratulations !!! You Won")
                    yesno = messagebox.askyesno("Play Again","Do you wanna Play Again")
                    if yesno:
                        self.frame3.pack_forget()
                        self.frame2.pack(fill="both", expand=True)

            else:
                buttons[row][col].config(bg ='red')
                buttons[row][col].config(width=15)
                buttons[row][col].config(height=6)
                self.stack.append([row,col])
                self.cond = 1 
                messagebox.showwarning("Conflict","Conflict occured, do backtrack by using Undo button")       
            

    def backtracking(self):
        print(self.stack)
        try:
            backstep = self.stack[-1]
            if self.stack:
                self.stack.pop()
                if self.cond == 0:    
                    buttons[backstep[0]][backstep[1]].config(image='')
                    self.board[backstep[0]][backstep[1]]=0
                    buttons[backstep[0]][backstep[1]].config(width=15)
                    buttons[backstep[0]][backstep[1]].config(height=6)
            
                else:
                    buttons[backstep[0]][backstep[1]].config(bg='white' if (backstep[0] + backstep[1]) % 2 else 'black' )
                    self.cond = 0
        except:
            print('nothing')
            


            
    def create_grid(self,frame3, rows, columns):
        global buttons
        buttons = [[None for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                button = tk.Button(frame3 ,command=lambda row=i, col=j: self.change_color(row, col), width=15, height=6, 
                                bg='white' if (i+j)%2  else 'black')
                
                button.grid(row=i, column=j)
                buttons[i][j] = button
        
        
                
        backButton =  tk.Button(self.frame3, text='UNDO',width = 10 ,height = 6,bg= 'white', command=self.backtracking )
        backButton.place(x= 910, y=20, )
        
    
        menubutton =  tk.Button(self.frame3, text='MENU',width = 10 ,height = 6,bg= 'white', command = self.menubtn)
        menubutton.place(x= 910, y=120)
    
    def menubtn(self):        
        self.frame3.pack_forget()
        self.frame2.pack(fill="both", expand=True)




    
from tkinter import PhotoImage
from PIL import Image, ImageTk

class MainGame:
    def __init__(self,N):
        self.N = N


    def start_game(self,root,frame2):
            
        self.root = root
        self.root.title("Button Grid")
        self.root.resizable(width=False,height=False)
        self.root.config(bg="green")
        self.root.geometry('1000x700')
        
        self.frame3 =  tk.Frame(self.root,width=1000, height=700)
        self.frame3.pack(fill="both", expand=True)  
        

        self.img = Image.open("F:\PycharmProjects\SEMESTER AI\imagssssss.png")
        self.img = self.img.resize((1000,700))

        bg = ImageTk.PhotoImage( self.img) 


        # Show image using label 
        label1 = tk.Label( self.frame3, image = bg) 
        label1.place(x = 0,y = 0) 
        # self.root.config()
        # frame1 = tk.Frame(self.root,height=700, width=1000)
        # frame1.place(x = 0,y =0)

        game = NqueenGame(self.N,self.frame3, frame2)
        game.create_grid(self.frame3, self.N, self.N)
        self.root.mainloop()

# startgame=  MainGame(6)
# startgame.start_game()
