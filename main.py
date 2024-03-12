import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image
from PIL import ImageTk

from game import MainGame

class NQueensFrontPage:
    def __init__(self):
        self.root = tk.Tk()
    
        self.root.title("N-Queens Game")
        self.root.resizable(width=False,height=False)
        self.root.geometry("896x672")

        img = Image.open("imagssssss.png")
        img = img.resize((1000, 700), Image.ADAPTIVE)
        self.bg = ImageTk.PhotoImage(img)

        self.canvas1 = tk.Frame(self.root, width=1000, height=700)
        # self.canvas1.place(x=0,y=0)
        # self.canvas1.create_image(0, 0, image=self.bg, anchor="nw")
        
        self.canvas1.pack(fill="both", expand=True)  
        labe1= tk.Label(self.canvas1, image= self.bg)
        labe1.place(x=0,y=0)
        
        play_img = Image.open("play.png")
        play_img = play_img.resize((150, 50), Image.ADAPTIVE)
        self.play_img = ImageTk.PhotoImage(play_img)

        button_x = (896 - 150) // 2 
        button_y = 550  
        self.move = tk.Button(self.canvas1, image=self.play_img, height=50, width=150)
        self.move.place(x=button_x, y=button_y)
        
        
        def open_new_canvas():
            self.canvas1.pack_forget()
            self.canvas2.pack(fill="both", expand=True)

        self.move.config(command=open_new_canvas)
        can2bg = Image.open("queenji.png")
        can2bg = can2bg.resize((896, 672), Image.ADAPTIVE)
        self.can2g = ImageTk.PhotoImage(can2bg)
        self.canvas2 = tk.Frame(self.root, width=1000, height=700)
        # self.canvas2.create_image(0, 0, image=self.can2g, anchor="nw")
        label2= tk.Label(self.canvas2, image= self.bg)
        label2.place(x=0,y=0)

        options_list = [4, 5, 6, 7]
        value_inside = tk.StringVar(self.canvas2)
        value_inside.set("Select an Option")
        
        
        def option_selected():
            try :
                selected_option = int(value_inside.get())
            except ValueError as e:
                messagebox.showerror('Value Error', "Select any option ")
                
            print(selected_option,type(int(selected_option)))
            messagebox.showinfo("Option Selected", f"You selected: {selected_option}")
            self.canvas2.pack_forget()
            

            gmae = MainGame(selected_option)
            gmae.start_game(self.root, self.canvas2)

        
        board = tk.Label(self.canvas2, text = "Select Board Dimensions NxN", foreground='white',bg ="black", font=50)
        board.place(x= 500 , y=300)
        
        option_menu = tk.OptionMenu(self.canvas2, value_inside, *options_list)
        # option_menu.config(height=3, width=30,font=50,foreground='black',bg ="#D30000")

        option_menu.config(height=3, width=30,font=50,foreground='white',bg ="black")
        option_menu.place(x= 500 , y=336)
        


        play_button = tk.Button(self.canvas2, text="Play", 
                                foreground='white',bg ="black",command=option_selected, height=3, width=30, font =50) 
        play_button.place(x=520 , y=430)
        
    def print_answers(self):
        print("Selected Option: {}".format(self.value_inside.get())) 

        return None
    
    def cavas2(self):
        tk.Canvas.delete()     
    
if __name__ == "__main__":
    front_page = NQueensFrontPage()
    front_page.root.mainloop()
    
    

