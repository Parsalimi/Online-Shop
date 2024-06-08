import tkinter as tk
from tkinter import messagebox

def display_product():
    product_name = "Echo Dot (3rd Gen) - Smart speaker with Alexa"
    product_price = "$39.99"
    product_image = "https://images-na.ssl-images-amazon.com/images/I/61W0K2YZ1xL._SL1000_.jpg"

    product_window = tk.Toplevel(root)
    product_window.title("Amazon Product")

    product_label = tk.Label(product_window, text=product_name, font=("Arial", 20))
    product_label.pack(pady=20)

    price_label = tk.Label(product_window, text=product_price, font=("Arial", 16))
    price_label.pack(pady=10)

    image_label = tk.Label(product_window, image=product_image, font=("Arial", 16))
    image_label.pack(pady=10)

    ok_button = tk.Button(product_window, text="OK", command=product_window.destroy, font=("Arial", 14))
    ok_button.pack(pady=20)

root = tk.Tk()
root.title("Amazon Sample")

welcome_label = tk.Label(root, text="Welcome to Amazon!", font=("Arial", 24))
welcome_label.pack(pady=50)

product_button = tk.Button(root, text="View Product", command=display_product, font=("Arial", 18))
product_button.pack(pady=20)

root.mainloop()