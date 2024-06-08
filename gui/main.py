import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from PIL import Image, ImageTk

class OnlineShop:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900")
        self.root.title("Online Shop")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.navigation_bar()
        self.display_items()

    def clear_current_panel(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def on_enter(event):
        event.widget.config(fg="blue", cursor="hand2")

    def on_leave(event):
        event.widget.config(fg="black", cursor="") 
    
    def navigation_bar(self):
        nav_frame = tk.Frame(self.main_frame)
        nav_frame.pack()

        # Create the navigation bar frame
        nav_bar = tk.Frame(self.main_frame, bg="lightgray", height=50)
        nav_bar.pack(fill=tk.X)

        # List of navigation items
        nav_items = [["Cart",self.display_cart_menu], 
                     ["Sign In",self.display_sign_in_menu],
                     ["Sign Up",self.display_cart_menu],
                     ["Categories",self.display_cart_menu],
                     ["Search",self.display_cart_menu],
                     ["Customer Service",self.display_cart_menu],
                     ["Gift Cards",self.display_cart_menu],
                     ["Sell",self.display_cart_menu]]

        # Create navigation labels
        for item_name, item_func in nav_items:
            label = tk.Label(nav_bar, text=item_name, font=("Helvetica", 14), bg="lightgray", fg="black", padx=10)
            label.pack(side=tk.LEFT, padx=10)
            label.bind("<Button-1>", lambda e, func=item_func: func())
            label.bind("<Enter>", OnlineShop.on_enter)
            label.bind("<Leave>", OnlineShop.on_leave)

    def display_cart_menu(self):
        self.clear_current_panel()
    
    def display_sign_in_menu(self):
        self.clear_current_panel()

        sign_in_frame = tk.Frame(self.main_frame)
        sign_in_frame.pack(expand=True, fill='both')

        # Create admin login panel within the frame
        tk.Label(sign_in_frame, text="Admin Login", font=("Helvetica", 16)).pack(pady=20)

        username_label = tk.Label(sign_in_frame, text="Username:")
        username_label.pack(pady=5)
        username_entry = tk.Entry(sign_in_frame)
        username_entry.pack(pady=5)

        password_label = tk.Label(sign_in_frame, text="Password:")
        password_label.pack(pady=5)
        password_entry = tk.Entry(sign_in_frame, show="*")
        password_entry.pack(pady=5)

        login_button = tk.Button(sign_in_frame, text="Login", command=lambda: self.login(username_entry, password_entry))
        login_button.pack(pady=10)

    def login(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
        if username == 'admin' and password == '12345':
            messagebox.showinfo("Login Info", "Welcome Admin")
        else:
            messagebox.showerror("Login Info", "Incorrect credentials")

    def display_items(self):
        canvas = tk.Canvas(self.main_frame)
        scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Bind mouse wheel events to the canvas
        self.root.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event, canvas))
        self.root.bind_all("<Button-4>", lambda event: self._on_mousewheel(event, canvas))
        self.root.bind_all("<Button-5>", lambda event: self._on_mousewheel(event, canvas))

        # Sample items
        items = ["Item 1", "Item 2", "Item 3", "Item 4"]

        # Load the image using Pillow
        image_path = "img1.png"  # Replace with your image path
        image = Image.open(image_path)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)

        for item_name in items:
            item_frame = ttk.Frame(scrollable_frame, relief="flat")
            item_frame.pack(side='left')

            image_label = ttk.Label(item_frame, image=photo)
            image_label.image = photo  # Keep a reference to the image
            image_label.pack(side=tk.TOP)

            item_label = ttk.Label(item_frame, text=item_name, font=("Helvetica", 14))
            item_label.pack(anchor="s")



        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


    def _on_mousewheel(self, event, canvas):
        if event.num == 5 or event.delta == -120:
            canvas.yview_scroll(1, "units")
        if event.num == 4 or event.delta == 120:
            canvas.yview_scroll(-1, "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineShop(root)
    root.mainloop()
