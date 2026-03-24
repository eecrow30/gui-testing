
import tkinter as tk
from tkinter import messagebox



root = tk.Tk()
root.title("To-Do List")
root.geometry("480x550")
root.configure(bg='pale green')

tk.Label(root,text="Input a task and click [ADD]:",
         fg="forest green",     ## instruction label so user knows what to do
         font=("Comic Sans MS",14)).pack(pady=(20,5))




#### ENTRY FIELD
task_entry = tk.Entry(root, width=32, font=("Comic Sans MS", 14),fg="forest green")
task_entry.pack(pady=5)

status = tk.Label(root,text="",font = ("Comic Sans MS", 10))
status.pack()

def add_task():
    task = task_entry.get().strip().title()
    if not task:
        status.config(test="Please enter a task", fg="forest green")
        task_entry.focus_set()
        return
    task_list.insert(tk.END,task)
    task_entry.delete(0,tk.END)
    task_entry.focus_set()
    status.config(text="Task added successfully!", fg="forest green")
    root.after(3000,lambda: status.config(text=""))


#### TASK LIST

task_list = tk.Listbox(root,width=36,height=12,
                       font=("Comic Sans MS", 14),
                       selectbackground="lawn green",
                       selectforeground="pale green")

task_list.pack(pady=10)



def delete_task():
    sel = task_list.curselection()
    if not sel:
        status.config(text="Select a task first.", fg="forest green")
        return
    if messagebox.askyesno("Confirm", "Delete this task?"):
        task_list.delete(sel[0])
        status.config(text="Task deleted.", fg="forest green")
        root.after(3000, lambda: status.config(text=""))

def mark_complete():
    sel = task_list.curselection()
    if not sel:
        status.config(text="Select a task first.", fg="red")
        return
    idx = sel[0]
    text = task_list.get(idx)
    if text.startswith("✓ "):
        status.config(text="Task already completed.", fg="orange")
        return
    task_list.delete(idx)
    task_list.insert(idx, "✓ " + text)
    status.config(text="Task marked complete!", fg="green")
    root.after(3000, lambda: status.config(text=""))


btn_style = {"font": ("Arial", 11), "width": 14}


btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Add Task",
    command=add_task, **btn_style).grid(row=0, column=0, padx=3)
tk.Button(btn_frame, text="Delete Task",
    command=delete_task, **btn_style).grid(row=0, column=1, padx=3)
tk.Button(btn_frame, text="Mark Complete",
    command=mark_complete, **btn_style).grid(row=1, column=0,
    columnspan=2, pady=5)
# H7: Flexibility — Enter key as shortcut for adding tasks
task_entry.bind("<Return>", lambda e: add_task())


root.mainloop()
