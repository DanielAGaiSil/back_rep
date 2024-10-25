import tkinter as tk
from tkinter import messagebox, simpledialog

class ExpenseManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Categorizer")
        self.root.geometry("600x450")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.necessary_expenses = {}
        self.optional_expenses = {}

        self.label_expense = tk.Label(root, text="Enter Expense Name:")
        self.label_expense.grid(row=0, column=0)
        self.entry_expense = tk.Entry(root)
        self.entry_expense.grid(row=0, column=1)

        self.label_amount = tk.Label(root, text="Enter Expense Amount:")
        self.label_amount.grid(row=1, column=0)
        self.entry_amount = tk.Entry(root)
        self.entry_amount.grid(row=1, column=1)

        self.category_var = tk.StringVar(value="necessary")
        self.radio_necessary = tk.Radiobutton(root, text="Necessary", variable=self.category_var, value="necessary")
        self.radio_necessary.grid(row=2, column=0)
        self.radio_optional = tk.Radiobutton(root, text="Optional", variable=self.category_var, value="optional")
        self.radio_optional.grid(row=2, column=1)

        self.submit_button = tk.Button(root, text="Submit Expense", command=self.submit_expense)
        self.submit_button.grid(row=3, column=0, columnspan=2)

        self.show_button = tk.Button(root, text="Show Categorized Expenses", command=self.show_expenses)
        self.show_button.grid(row=4, column=0, columnspan=2)

    def submit_expense(self):

        expense_name = self.entry_expense.get()
        expense_amount = self.entry_amount.get()
        category = self.category_var.get()

        try:
            expense_amount = float(expense_amount)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the expense amount.")
            return

        if category == 'necessary':
            self.necessary_expenses[expense_name] = expense_amount
        elif category == 'optional':
            self.optional_expenses[expense_name] = expense_amount

        self.entry_expense.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

    def show_expenses(self):

        necessary_message = "Necessary Expenses:\n"
        for expense, amount in self.necessary_expenses.items():
            necessary_message += f"{expense}: ${amount:.2f}\n"

        optional_message = "Optional Expenses:\n"
        for expense, amount in self.optional_expenses.items():
            optional_message += f"{expense}: ${amount:.2f}\n"

        full_message = necessary_message + "\n" + optional_message
        messagebox.showinfo("Categorized Expenses", full_message)

root = tk.Tk()
app = ExpenseManager(root)
root.mainloop()
