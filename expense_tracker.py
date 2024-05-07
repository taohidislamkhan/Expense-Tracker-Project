import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import matplotlib.patches as patches
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import csv
from datetime import datetime
from os.path import exists

class LoginApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")
        self.master.geometry("1366x768")
        self.master.configure(bg="#333333")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.users = {}
        self.load_users_from_csv()
        self.create_widgets()

    def create_widgets(self):
        self.create_login_interface()

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if  str(self.users[username]["password"]) == str(password):
           self.open_dashboard(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def open_dashboard(self, username):
        self.master.withdraw()
        dashboard_root = tk.Toplevel(self.master)
        dashboard_root.protocol("WM_DELETE_WINDOW", lambda: self.master.quit())
        app = Widget(dashboard_root, username)

    def create_signup_interface(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.money_image = Image.open('money.jpeg')
    
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
            
        self.money_image = self.money_image.resize((window_width, window_height), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.money_image)
        self.image_label = tk.Label(self.master, image=self.tk_image)
        self.image_label.place(x=0, y=0)

        signup_label = ttk.Label(self.master, text="SIGN UP", font=("Times", "36", "bold italic"),
                                 background="#FFFFFF",foreground="#333333")
        signup_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.username_label = ttk.Label(self.master, text="Username:", font=("Helvetica", "20"),
                                        background="#FFFFFF",foreground="#333333")
        self.username_label.grid(row=2, column=0, padx=(100, 20), pady=(100, 10), sticky=tk.E)
        self.username_entry = ttk.Entry(self.master, width=30, font=("Helvetica", "20"))
        self.username_entry.grid(row=2, column=1, padx=(0, 100), pady=(100, 10), sticky=tk.W)

        self.password_label = ttk.Label(self.master, text="Password:", font=("Helvetica", "20"),
                                        background="#FFFFFF",foreground="#333333")
        self.password_label.grid(row=3, column=0, padx=(100, 20), pady=10, sticky=tk.E)
        self.password_entry = ttk.Entry(self.master, show="*", width=30, font=("Helvetica", "20"))
        self.password_entry.grid(row=3, column=1, padx=(0, 100), pady=10, sticky=tk.W)

        self.confirm_password_label = ttk.Label(self.master, text="Confirm Password:", font=("Helvetica", "20"),
                                                background="#FFFFFF",foreground="#333333")
        self.confirm_password_label.grid(row=4, column=0, padx=(100, 20), pady=10, sticky=tk.E)
        self.confirm_password_entry = ttk.Entry(self.master, show="*", width=30, font=("Helvetica", "20"))
        self.confirm_password_entry.grid(row=4, column=1, padx=(0, 100), pady=10, sticky=tk.W)

        self.signup_button = ttk.Button(self.master, text="Sign Up", command=self.register_user, style="T.TButton")
        self.signup_button.grid(row=6, column=0, columnspan=2, padx=20, pady=(50))

        self.back_button = ttk.Button(self.master, text="Back to Login", command=self.create_login_interface)
        self.back_button.grid(row=7, column=0, columnspan=2, padx=20, pady=(20))

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if username in self.users:
            messagebox.showerror("Error", "Username already exists")
            return

        self.users[username] = {"password": password}
        self.save_users_to_csv()
        messagebox.showinfo("Success", "User registered successfully!")

        self.create_login_interface()

    def load_users_from_csv(self):
        try:
            df = pd.read_csv('users.csv')
            for index, row in df.iterrows():
                self.users[row["username"]] = {"password": row["password"]}

        except FileNotFoundError:
            pass

    def save_users_to_csv(self):
        df = pd.DataFrame.from_dict(self.users, orient='index', columns=["password"])
        
        df.to_csv("users.csv", index_label="username")

    def create_login_interface(self):
        for widget in self.master.winfo_children():
         widget.destroy()
        
        self.master.update_idletasks()
        self.money_image = Image.open('money.jpeg')
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
        self.money_image = self.money_image.resize((window_width, window_height), Image.LANCZOS)

        self.tk_image = ImageTk.PhotoImage(self.money_image)
        self.image_label = tk.Label(self.master, image=self.tk_image)
        self.image_label.place(x=0, y=0)

        login_label = ttk.Label(self.master, text="LOG IN", font=("Times", "36", "bold italic"),
                        background="#FFFFFF",foreground="#0000FF")
        login_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.username_label = ttk.Label(self.master, text="Username:", font=("Helvetica", "20"),
                                background="#FFFFFF",foreground="#333333")
        self.username_label.grid(row=2, column=0, padx=(100, 20), pady=(100, 10), sticky=tk.E)
        self.username_entry = ttk.Entry(self.master, width=30, font=("Helvetica", "20"))
        self.username_entry.grid(row=2, column=1, padx=(0, 100), pady=(100, 10), sticky=tk.W)

        self.password_label = ttk.Label(self.master, text="Password:", font=("Helvetica", "20"),
                                background="#FFFFFF",foreground="#333333")
        self.password_label.grid(row=3, column=0, padx=(100, 20), pady=10, sticky=tk.E)
        self.password_entry = ttk.Entry(self.master, show="*", width=30, font=("Helvetica", "20"))
        self.password_entry.grid(row=3, column=1, padx=(0, 100), pady=10, sticky=tk.W)

        self.login_button = ttk.Button(self.master, text="Login", command=self.validate_login, style="T.TButton")
        self.login_button.grid(row=4, column=0, columnspan=2, padx=20, pady=(50))

        self.signup_button = ttk.Button(self.master, text="Sign Up", command=self.create_signup_interface)
        self.signup_button.grid(row=6, column=0, columnspan=2, padx=20, pady=(20))

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.username_entry.focus_set()

    def open_dashboard(self, username):
        self.master.withdraw()

        dashboard_root = tk.Toplevel(self.master)
        dashboard_root.protocol("WM_DELETE_WINDOW", lambda: self.master.quit())  # Ensure entire app closes properly

        app = Widget(dashboard_root)
        app.pack(fill="both", expand=True)

class Widget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
       
        self.items = 0
        self._data = {}
        self.total_expenses = tk.StringVar()
        self.total_expenses.set(f"Total Expenses: {self._data}")

        self.configure(background="#CBC3E3")
        self.fig = None
        self.canvas = None 

        self.load_data_from_csv()
        self.create_widgets()
        self.fill_table()

    def create_widgets(self):
        self.table = ttk.Treeview(self, columns=("Description", "Price", "Date & Time"),show="headings",
                                  style="Custom.Treeview")
        self.table.heading("Description", text="Description")
        self.table.heading("Price", text="Price")
        self.table.heading("Date & Time", text="Date & Time")

        self.table.column("Description", width=15)
        self.table.column("Price", width=15)
        self.table.column("Date & Time", width=15)

        self.table.tag_configure('oddrow', background='#E8E8E8')
        self.table.tag_configure('evenrow', background='#DFDFDF')

        self.table.pack(side="left", fill="both", expand=True)

        right_frame = tk.Frame(self, background="#AEB6BF")

        tk.Label(right_frame, text="Description:", background="#AEB6BF", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.description = tk.Entry(right_frame, font=("Helvetica", 12))
        self.description.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(right_frame, text="Price (BDT):", background="#AEB6BF", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.price = tk.Entry(right_frame, font=("Helvetica", 12))
        self.price.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.add = tk.Button(right_frame, text="Add", command=self.add_element, font=("Helvetica", 12), bg="#229954", fg="white")
        self.add.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

        self.plot = tk.Button(right_frame, text="Plot", command=self.plot_data, font=("Helvetica", 12), bg="#2E86C1", fg="white")
        self.plot.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

        tk.Label(right_frame, textvariable=self.total_expenses, background="#AEB6BF", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        right_frame.pack(side="right", fill="y")

    def add_element(self):
        des = self.description.get().strip()
        price = self.price.get().strip()

        if not des:
            messagebox.showerror("Error", "Please enter a description.")
            return

        try:
            price_float = float(price)
            if price_float <= 0:
                raise ValueError("Price must be greater than zero.")
            
            now = datetime.now()
            current_time = f"Date: {now.strftime('%d-%m-%Y')}, Time: {now.strftime('%H:%M:%S')}"

            tag = 'evenrow' if self.items % 2 == 0 else 'oddrow'
            self.items += 1

            self.table.insert("", "end", values=(des, f"{price_float:.2f}", current_time), tags=(tag,))
            self.description.delete(0, "end")
            self.price.delete(0, "end")
            self.update_total_expenses(price_float)
            self.save_to_csv(des, price_float, current_time)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_data_from_csv(self):
        try:
            df = pd.read_csv('expenses.csv')
            if 'description' in df.columns and 'price' in df.columns and 'timestamp' in df.columns:
                self._data = []
                for index, row in df.iterrows():
                    self._data.append({
                        'description': row['description'],
                        'price': row['price'],
                        'timestamp': row['timestamp']
                    })
            else:
                messagebox.showerror("Error", "CSV file does not contain required columns.")
        except FileNotFoundError:
            messagebox.showerror("Error", "File 'expenses.csv' not found.")

    def save_to_csv(self, description, price, timestamp):
        try:
            data = {
                'description': [description],
                'price': [price],
                'timestamp': [timestamp]
            }
            df = pd.DataFrame(data)
            
            if not exists('expenses.csv'):
                df.to_csv('expenses.csv', index=False)
            else:
                df.to_csv('expenses.csv', mode='a', header=False, index=False)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save to CSV: {e}")

    def update_total_expenses(self, price):
        total = sum(float(self.table.item(item, "values")[1]) for item in self.table.get_children())
        self.total_expenses.set(f"Total Expenses: {total:.2f}")

    def plot_data(self):
        if self.fig:
            self.fig.clear()

        labels = []
        sizes = []
        for item in self.table.get_children():
            if self.fig:
                self.fig.clear()
                self.fig = Figure(figsize=(8, 6), dpi=100, facecolor='#301934')
                self.ax = self.fig.add_subplot(111)
                self.canvas = FigureCanvasTkAgg(self.fig, master=self)
                self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            values = self.table.item(item, "values")
            labels.append(values[0])
    
            price_str = values[1]
            sizes.append(float(price_str))

        if not labels:
            messagebox.showinfo("Info", "No data to plot.")
            return

        if not self.fig:
            self.fig = Figure(figsize=(8, 6), dpi=100, facecolor="#E6E6FA")
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        else:
            self.ax.clear()

        self.ax.bar(labels, sizes, color='red')
        self.ax.set_ylabel('Amount (BDT)', fontsize=12)
        self.ax.set_xlabel('Item Description', fontsize=12)
        self.ax.set_title('Expense Breakdown', fontsize=14)

        for i, size in enumerate(sizes):
            self.ax.text(i, size, f"{size:.2f}", ha='center', va='bottom', fontsize=10)

        self.canvas.draw()

    def fill_table(self):
        self.items = 0  # Reset item count when filling table
        for dic in self._data:
            tag = 'evenrow' if self.items % 2 == 0 else 'oddrow'
            self.items += 1
            self.table.insert("", "end", values=(dic['description'], f"{dic['price']:.2f}", dic['timestamp']), tags=(tag,))
            self.update_total_expenses(0)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("1366x768")
        self.configure(background="#CBC3E3")
        style = ttk.Style(self)
        style.configure("Custom.Treeview", background="#CBC3E3", foreground="black", fieldbackground="#CBC3E3")

        self.widget = Widget(self)
        self.widget.pack(fill="both", expand=True)
    

def main():
    root = tk.Tk()
    app = LoginApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()


