import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv

class LoginApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("1366x768")
        self.master.configure(bg="#333333")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.users = {}
        self.load_users_from_csv()  # Load existing user data from CSV

        self.create_widgets()

    def create_widgets(self):
        self.create_login_interface()

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in self.users and self.users[username]["password"] == password:
           self.open_dashboard(username)  # Open dashboard after successful login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def open_dashboard(self, username):
    # Hide the current login window
        self.master.withdraw()

    # Create a new top level window for the dashboard
        dashboard_root = tk.Toplevel(self.master)
        dashboard_root.protocol("WM_DELETE_WINDOW", lambda: self.master.quit())  # Ensure entire app closes properly

    # Initialize and run the dashboard application
        app = DashboardApplication(dashboard_root, username)

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
        self.save_users_to_csv()  # Save updated user data to CSV
        messagebox.showinfo("Success", "User registered successfully!")

        self.create_login_interface()

    def load_users_from_csv(self):
        try:
            with open("users.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.users[row["username"]] = {"password": row["password"]}
        except FileNotFoundError:
            # File does not exist, no users to load
            pass

    def save_users_to_csv(self):
        with open("users.csv", "w", newline="") as file:
            fieldnames = ["username", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for username, data in self.users.items():
                writer.writerow({"username": username, "password": data["password"]})

    def create_login_interface(self):
        for widget in self.master.winfo_children():
         widget.destroy()
        
        self.master.update_idletasks()
        # Resize the image to fit the window
        self.money_image = Image.open('money.jpeg')
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
        self.money_image = self.money_image.resize((window_width, window_height), Image.LANCZOS)

        self.tk_image = ImageTk.PhotoImage(self.money_image)
        self.image_label = tk.Label(self.master, image=self.tk_image)
        self.image_label.place(x=0, y=0)

        login_label = ttk.Label(self.master, text="LOGIN", font=("Times", "36", "bold italic"),
                        background="#FFFFFF",foreground="#333333")
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
        # Close the current window
        self.master.destroy()

        # Open the dashboard window
        root = tk.Tk()
        app = DashboardApplication(root, username)
        root.mainloop()

class DashboardApplication:
    def __init__(self, master, username):
        self.master = master
        self.master.title("Dashboard - Daily Expense Tracker")
        self.master.geometry("800x600")
        self.master.configure(bg="#333333")

        self.username = username
        
        # Set up the user interface for the expense tracker
        self.create_widgets()

    def create_widgets(self):
        # Adding expense form
        ttk.Label(self.master, text=f"Hello, {self.username}!", font=("Helvetica", 18), background="#333333", foreground="#FFFFFF").pack(pady=10)

        # Frame for adding expenses
        frame = ttk.Frame(self.master)
        frame.pack(pady=20)

        ttk.Label(frame, text="Amount: ", font=("Helvetica", 16)).grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = ttk.Entry(frame, font=("Helvetica", 16), width=20)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Category: ", font=("Helvetica", 16)).grid(row=1, column=0, padx=10, pady=10)
        self.category_entry = ttk.Entry(frame, font=("Helvetica", 16), width=20)
        self.category_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Date (YYYY-MM-DD): ", font=("Helvetica", 16)).grid(row=2, column=0, padx=10, pady=10)
        self.date_entry = ttk.Entry(frame, font=("Helvetica", 16), width=20)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = ttk.Button(frame, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Section for displaying expenses
        self.expenses_frame = ttk.Frame(self.master)
        self.expenses_frame.pack(pady=20)
        self.update_expense_list()

    def add_expense(self):
        # Implement functionality to add the expense to some form of persistent storage
        print("Expense Added:", self.amount_entry.get(), self.category_entry.get(), self.date_entry.get())
        # For now just printing to console
        # You should integrate it with a database or a file
        self.update_expense_list()

    def update_expense_list(self):
        # This function would update or refresh the list of expenses displayed
        for widget in self.expenses_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.expenses_frame, text="List of Recent Expenses:", font=("Helvetica", 16)).pack()
        # Display expenses; this is just a placeholder
        ttk.Label(self.expenses_frame, text="No expenses recorded yet.", font=("Helvetica", 14)).pack()

    def open_dashboard(self, username):
        # Close the current window
        self.master.destroy()

        # Open the dashboard window
        root = tk.Tk()
        app = DashboardApplication(root, username)
        root.mainloop()
        

def main():
    root = tk.Tk()
    app = LoginApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()

