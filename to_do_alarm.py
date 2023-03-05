import tkinter as tk
from datetime import datetime, timedelta


class TodoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do Alarm")

        # Here we make the tasks entry and due date if there is one
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(master, width=20)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.remind_check = tk.Checkbutton(master, text="Remind me")
        self.remind_check.grid(row=0, column=2, padx=5, pady=5)

        # task list
        self.task_list = tk.Listbox(master, height=15, width=50)
        self.task_list.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # delete and add tasks
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        self.del_button = tk.Button(master, text="Remove Task", command=self.delete_task)
        self.del_button.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.master, text="Exit", command=self.master.quit).grid(row=2, column=2)

    # add and delete tasks
    def add_task(self):
        task = self.task_entry.get()
        due_date_str = self.date_entry.get()

        if due_date_str:
            due_date = datetime.strptime(due_date_str, "%d/%m/%Y %I:%M %p")
            remind = self.remind_check.get()
            if remind:
                self.set_reminder(due_date, task)
            else:
                pass
            seconds_until_due = (due_date - datetime.now()).total_seconds()
        else:
            secounds_until_due = None

        self.task_list.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def delete_task(self):
        index = self.task_list.curselection()
        if index:
            self.task_list.delete(index)

    def set_reminder(self, due_date, task):
        seconds_until_reminder = (due_date - datetime.now() - timedelta(minutes=15)).total_seconds()
        if seconds_until_reminder > 0:
            self.master.after(int(seconds_until_reminder * 1000), self.show_reminder, task)

    def show_reminder(self, task):
        reminder_window = tk.Toplevel(self.master)
        reminder_window.title("You have to do this ")
        reminder_lable = tk.Label(reminder_window, text=f"Do that: {task}")
        reminder_lable.pack()


if __name__ == "__main__":
    root = tk.Tk()
    todo_list = TodoList(root)
    root.mainloop()
