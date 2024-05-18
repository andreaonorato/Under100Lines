import tkinter as tk

def add_task():
    """Function to add a task to the to-do list."""
    task = entry.get()
    if task.strip() != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    """Function to delete a selected task from the to-do list."""
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
        save_tasks()

def save_tasks():
    """Function to save tasks to an external text file."""
    with open("tasks.txt", "w") as f:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create listbox to display tasks
listbox = tk.Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

# Load tasks from external text file
try:
    with open("tasks.txt", "r") as f:
        for task in f:
            listbox.insert(tk.END, task.strip())
except FileNotFoundError:
    pass

# Create entry for new tasks
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Create buttons to add and delete tasks
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.pack(side=tk.LEFT, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Run the application
root.mainloop()
