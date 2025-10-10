import tkinter as tk
from tkinter import messagebox
import pygame as pg

class Method:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.result_list = []
        
    def string_show(self, *args):
        
        font = pg.font.SysFont('Arial', 15)
        if len(args) == 1:
            text = f"{args[0]}"
        elif len(args) == 2:
            text = f"{args[0]} {args[1]:>6.3f}"
        elif len(args) == 4:
            text = f"{args[0]} ({args[1]:>6.3f}, {args[2]:>6.3f}, {args[3]:>6.3f})"
        else:
            text = f"{args[0]}"
        return font.render(text, True, (255, 255, 255))
    
    def submit(self, window, *args):
        try:
            pos = [float(args[0].get()), float(args[1].get()), float(args[2].get())]
            vel = [float(args[3].get()), float(args[4].get()), float(args[5].get())]
            mas = float(args[6].get())
            rad = float(args[7].get())
            col = [int(args[8].get()), int(args[9].get()), int(args[10].get()), float(args[11].get())]
            
            for i in col[:3]:
                if not(0 <= i <= 255):
                    messagebox.showerror("Error", "Colors must be between 0 and 255")
                    return
                
            if not(0.0 <= col[3] <= 1.0):
                messagebox.showerror("Error", "Alpha must be between 0.0 and 1.0")
                return
                
            if mas <= 0:
                messagebox.showerror("Error", "Mass must be greater than 0")
                return
                
            if rad <= 0:
                messagebox.showerror("Error", "Radius must be greater than 0")
                return
                
            self.result_list = [pos, vel, mas, rad, col]
            window.destroy()
            
        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers")
            
    def show_add_form(self):
        window = tk.Tk()
        window.title("Add New Object")
        window.geometry("300x500")

        labels = ["Position X:", "Position Y:", "Position Z:", "Velocity X:", "Velocity Y:", "Velocity Z:", "Mass:", "Radius:", "Color R:", "Color G:", "Color B:", "Alpha:"]
        entries = []
        
        for i, label_text in enumerate(labels):
            label = tk.Label(window, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)
            
        submit_button = tk.Button(window, text="Add", command=lambda: self.submit(window, *entries))
        submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)
        
        window.mainloop()