import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {"description": self.description, "completed": self.completed}

    @classmethod
    def from_dict(cls, data):
        return cls(data["description"], data["completed"])

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]

class TodoListGUI:
    def __init__(self, master):
        self.master = master
        self.todo_list = TodoList()

        master.title("To-Do List Application")
        master.geometry("400x300")

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.mark_completed_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed)
        self.mark_completed_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.refresh_task_list()

    def add_task(self):
        description = simpledialog.askstring("Add Task", "Enter task description:")
        if description:
            self.todo_list.add_task(description)
            self.refresh_task_list()

    def mark_completed(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.todo_list.mark_completed(index)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.todo_list.delete_task(index)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            status = "✓" if task.completed else " "
            self.task_listbox.insert(tk.END, f"[{status}] {task.description}")

def main():
    root = tk.Tk()
    todo_list_gui = TodoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
