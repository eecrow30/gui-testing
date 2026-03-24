
import tkinter as tk
from tkinter import messagebox

### defining colours for easier use throughout code
pgcol = "pale green"
fgcol = "forest green"
lgcol = "lime green"



root=tk.Tk()
root.title("To-Do List") ## title of the tab - shows at very top
root.geometry("480x550")


tk.Label(root,text="Enter a task and click [ADD]:",
         fg = fgcol, bg = pgcol, ## initial instruction label at top of screen
         font=("Georgia",14)).pack(pady=(15,5))     ## tells user what to do


#### ENTRY FIELD - below instruction label
enter_task = tk.Entry(root,width=32,font=("Georgia",15), fg=fgcol,bg=pgcol) ## allow user to input
enter_task.pack(pady=5)

status = tk.Label(root, text="",font=("Georgia",12), fg=fgcol,bg=pgcol) ## status label that updates to let the user know what is happening
status.pack()


#### ADD, DELETE, and MARK COMPLETE

def add_task():
    task = enter_task.get().strip().title() ### use of strip and title to make list look clean
    if not task:
        status.config(text="ERROR - Enter a task name.", fg=fgcol,bg=pgcol) ## validate input
        enter_task.focus_set()
        return
    task_list.insert(tk.END,task)
    enter_task.delete(0,tk.END)
    enter_task.focus_set()
    status.config(text="Task successfully added", fg=fgcol,bg=pgcol) 
    root.after(3000,lambda: status.config(text=""))

def delete_task():
    sel = task_list.curselection()
    if not sel:
        status.config(test="ERROR - Select a task first.", fg=fgcol,bg=pgcol) ## validation
        return
    if messagebox.askyesno("Confirm","Are you sure?"):  ## confirmation to allow user to go back
        task_list.delete(sel[0])
        status.config(text="Task successfully deleted",fg=fgcol,bg=pgcol)
        root.after(3000,lambda: status.config(text=""))

def mark_complete():
    sel = task_list.curselection()
    if not sel:
        status.config(text="ERROR - Select a task first.", fg=fgcol,bg=pgcol) ## validation
        return
    idx = sel[0]
    text= task_list.get(idx)
    if text.startswith("✓"):
        status.config(text="ERROR - Task already marked as complete.", fg=fgcol,bg=pgcol) ## validation
        return
    task_list.delete(idx)
    task_list.insert(idx,"✓"+text)
    status.config(text="Task successfully marked as complete", fg=fgcol,bg=pgcol)
    root.after(3000,lambda:status.config(text=""))



#### LIST BOX - displays below input box and status updates
task_list = tk.Listbox(root,width=36,height=12,
                       font=("Georgia",14),
                       fg=fgcol,bg=pgcol)
task_list.pack(pady=10)


#### BUTTONS - display below list box
btt_style = {"font":("Georgia",14),"width":15,"fg":fgcol,"bg":pgcol}
btt_frame=tk.Frame(root)
btt_frame.pack(pady=5)


tk.Button(btt_frame,text="ADD",
          command=add_task,**btt_style).grid(row=0,column=0,padx=3)
tk.Button(btt_frame,text="DELETE",
          command=delete_task,**btt_style).grid(row=0,column=1,padx=3)
tk.Button(btt_frame,text="MARK COMPLETE",
          command=mark_complete,**btt_style).grid(row=1,column=0,padx=3)


enter_task.bind("<Return>",lambda e: add_task)

#### EVENT LOOP
root.mainloop()



