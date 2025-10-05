import tkinter as tk
from tkinter import messagebox
import pygame as pg
import threading

import gui.body as bd


# Utility methods for GUI operations
class Method:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.result_list = []

    def adjust_context_cas(self, obj_cas, screen_cas):
        # Adjust context menu position to stay within screen bounds
        if obj_cas[0] + obj_cas[2] > screen_cas[2] + screen_cas[0]:
            obj_cas[0] -= obj_cas[2]
        if obj_cas[1] + obj_cas[3] > screen_cas[3] + screen_cas[1]:
            obj_cas[1] -= obj_cas[3]
        return [obj_cas[0], obj_cas[1], obj_cas[2], obj_cas[3]]
    
    def string_show(self, *args):
        # Create a rendered string object for display
        string = ''
        for arg in args:
            string = string + " " + str(arg)
        small_font_style = pg.font.SysFont('Helvetica', 15)
        str_obj = small_font_style.render(string, True, (255, 255, 255), (0, 0, 0))
        return str_obj

    def show_add_form(self):
        # Display form for adding new bodies to simulation
        root = tk.Tk()
        root.title("Body Attributes")

        tk.Label(root, text="Position:", width=10).grid(row=0, column=0, sticky="w")
        x_entry = tk.Entry(root, width=10); x_entry.grid(row=0, column=1)
        y_entry = tk.Entry(root, width=10); y_entry.grid(row=0, column=2)
        z_entry = tk.Entry(root, width=10); z_entry.grid(row=0, column=3)

        tk.Label(root, text="Velocity:", width=10).grid(row=1, column=0, sticky="w")
        i_entry = tk.Entry(root, width=10); i_entry.grid(row=1, column=1)
        j_entry = tk.Entry(root, width=10); j_entry.grid(row=1, column=2)
        k_entry = tk.Entry(root, width=10); k_entry.grid(row=1, column=3)

        tk.Label(root, text="Mass:", width=10).grid(row=2, column=0, sticky="w")
        mass_entry = tk.Entry(root, width=10); mass_entry.grid(row=2, column=1)

        tk.Label(root, text="Radius:", width=10).grid(row=3, column=0, sticky="w")
        radius_entry = tk.Entry(root, width=10); radius_entry.grid(row=3, column=1)
        
        tk.Label(root, text="Color:", width=10).grid(row=4, column=0, sticky="w")
        r_entry = tk.Entry(root, width=10); r_entry.grid(row=4, column=1)
        g_entry = tk.Entry(root, width=10); g_entry.grid(row=4, column=2)
        b_entry = tk.Entry(root, width=10); b_entry.grid(row=4, column=3)

        tk.Label(root, text="Alpha:", width=10).grid(row=5, column=0, sticky="w")
        alpha_entry = tk.Entry(root, width=10); alpha_entry.grid(row=5, column=1)

        def cancel():
            root.destroy()

        def submit():
            try:
                x, y, z = float(x_entry.get()), float(y_entry.get()), float(z_entry.get())
                i, j, k = float(i_entry.get()), float(j_entry.get()), float(k_entry.get())
                mass = float(mass_entry.get())
                radius = float(radius_entry.get())
                R, G, B = int(r_entry.get()), int(g_entry.get()), int(b_entry.get())
                A = float(alpha_entry.get())

                self.result_list = [[x, y, z], [i, j, k], mass, radius, [R, G, B, A]]
                messagebox.showinfo("Success", f"Added:\n{self.result_list}")
                root.destroy()  # Close form after adding
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
            # Note: Body integration would be handled by the GUI window

        tk.Button(root, text="Cancel", command=cancel, width=10).grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Add", command=submit, width=10).grid(row=6, column=2, columnspan=2, pady=5)

        root.mainloop()