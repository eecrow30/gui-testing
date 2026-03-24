
import tkinter as tk
from tkinter import messagebox



root = tk.Tk()
root.title("To-Do List")
root.geometry("420x480")
root.configure(bg='pale green')

tk.Label(root,text="Input a task and click [ADD]:",
         fg="forest green",     ## instruction label so user knows what to do
         font=("Comic Sans MS",11)).pack(pady=(20,5))






root.mainloop()
