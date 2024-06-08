import tkinter as tk
from tkinter import ttk

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
                     "Sign In", 
                     "Sign Up", 
                     "Categories",
                     "Search", 
                     "Customer Service", 
                     "Gift Cards", "Sell"]

        # Create navigation labels
        for item_name, item_func in nav_items:
            label = tk.Label(nav_bar, text=item_name, font=("Helvetica", 14), bg="lightgray", fg="black", padx=10)
            label.pack(side=tk.LEFT, padx=10)
            label.bind("<Button>", lambda e: item_func())
            label.bind("<Enter>", OnlineShop.on_enter)
            label.bind("<Leave>", OnlineShop.on_leave)

    def display_cart_menu(self):
        self.clear_current_panel()

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
        canvas.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event, canvas))
        canvas.bind_all("<Button-4>", lambda event: self._on_mousewheel(event, canvas))
        canvas.bind_all("<Button-5>", lambda event: self._on_mousewheel(event, canvas))

        # Sample items
        items = [("Item 1", "Description of Item 1"), ("Item 2", "Description of Item 2"),
                 ("Item 3", "Description of Item 3"), ("Item 4", "Description of Item 4")]

        for item_name, item_desc in items:
            item_frame = ttk.Frame(scrollable_frame, padding=10, relief="ridge")
            item_frame.pack(fill="x", pady=5)

            item_label = ttk.Label(item_frame, text=item_name, font=("Helvetica", 14))
            item_label.pack(anchor="w")

            desc_label = ttk.Label(item_frame, text=item_desc, font=("Helvetica", 10))
            desc_label.pack(anchor="w")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(self, event, canvas):
        # Windows and MacOS
        if event.delta:
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        # Linux systems
        elif event.num == 4:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineShop(root)
    root.mainloop()
