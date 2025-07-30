import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

# Functions for the GUI
def add_task():
    task = entry.get()
    if task:
        tasks.append({"description": task, "completed": False})
        entry.delete(0, tk.END)
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_completed():
    try:
        index = listbox.curselection()[0]
        tasks[index]["completed"] = True
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task["completed"] else "❌"
        listbox.insert(tk.END, f"{task['description']} [{status}]")

# GUI setup
tasks = load_tasks()
root = tk.Tk()
root.title("📝 To-Do List App")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

complete_btn = tk.Button(root, text="Mark as Completed", command=mark_completed)
complete_btn.pack()

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

update_listbox()
root.mainloop()