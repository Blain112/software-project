# Test

import tkinter as tk
import tkinter.messagebox as messagebox
import csv
from PIL import Image, ImageTk

# Define fonts
heading_font = ("Arial", 32, "bold")
label_font = ("Arial", 16, "bold")
entry_font = ("Arial", 12)
button_font = ("Arial", 16, "bold")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Brilliant Bank")

        container = tk.Frame(root)
        container.pack(fill="both", expand=True)

        # Allow container to stretch and center content
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LandingPage, SignupPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LandingPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Make this page fill and center content
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        # Heading
        heading = tk.Label(self, text="Brilliant Bank", font=heading_font)
        heading.grid(row=0, column=0, columnspan=3, pady=(20, 5), sticky="n")

        # Logo
        image = Image.open("brilliant_bank_logo.png")
        image = image.resize((80, 80))
        self.logo = ImageTk.PhotoImage(image)
        logo_label = tk.Label(self, image=self.logo)
        logo_label.grid(row=1, column=0, columnspan=3, pady=(0, 20), sticky="n")

        # Sign Up Button
        signup_button = tk.Button(self, text="Sign Up", font=button_font,
                                  command=lambda: controller.show_frame("SignupPage"))
        signup_button.grid(row=2, column=1, pady=10, sticky="n")


class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        # Heading
        heading = tk.Label(self, text="Brilliant Bank", font=heading_font)
        heading.grid(row=0, column=0, columnspan=3, pady=(20, 5), sticky="n")

        # Logo
        image = Image.open("brilliant_bank_logo.png")
        image = image.resize((80, 80))
        self.logo = ImageTk.PhotoImage(image)
        logo_label = tk.Label(self, image=self.logo)
        logo_label.grid(row=1, column=0, columnspan=3, pady=(0, 20), sticky="n")

        # === FORM FRAME (Centered) ===
        form_frame = tk.Frame(self)
        form_frame.grid(row=2, column=1, pady=(0, 20))

        # First Name
        self.first_name_label = tk.Label(form_frame, text="First Name", font=label_font)
        self.first_name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.first_name_entry = tk.Entry(form_frame, font=entry_font)
        self.first_name_entry.grid(row=1, column=0, padx=10, pady=5)

        # Password
        self.password_label = tk.Label(form_frame, text="Password", font=label_font)
        self.password_label.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        self.password_entry = tk.Entry(form_frame, font=entry_font, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Last Name
        self.last_name_label = tk.Label(form_frame, text="Last Name", font=label_font)
        self.last_name_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.last_name_entry = tk.Entry(form_frame, font=entry_font)
        self.last_name_entry.grid(row=3, column=0, padx=10, pady=5)

        # Confirm Password
        self.confirm_password_label = tk.Label(form_frame, text="Confirm Password", font=label_font)
        self.confirm_password_label.grid(row=2, column=1, sticky="w", padx=10, pady=5)
        self.confirm_password_entry = tk.Entry(form_frame, font=entry_font, show="*")
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Sign Up Button (Centered)
        signup_button = tk.Button(self, text="Sign Up", font=button_font, command=self.signup)
        signup_button.grid(row=3, column=1, pady=10)

    def signup(self):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()

        if not first_name or not last_name or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        with open('customers.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, password])

        messagebox.showinfo("Success", "New user account has been created.")
        self.clear_fields()

    def clear_fields(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)

# === Your Required Entry Point ===
if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    root.geometry("848x480")
    app = App(root)
    root.mainloop()
