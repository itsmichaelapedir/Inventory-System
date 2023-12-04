''' --------------------------------------------------------------------------------------------
learning materials and resources we used to build and develop our responsive Inventory System project:
https://www.geeksforgeeks.org/python-pillow-tutorial/ - helped with handling images in Python.
https://www.geeksforgeeks.org/python-gui-tkinter/ - how to make graphical interfaces.
https://realpython.com/python-gui-tkinter/ - guide on creating GUIs using Tkinter.
https://docs.python.org/3/ - official guide for Python programming.
https://www.w3schools.com/python/ - fundamental Python language knowledge.
https://openai.com/ - For dev challenges and logic errors: ask questions, seek guidance, get tips.
https://tinyurl.com/49fvb3fz - brocode YT channel, practical insights into Python.
https://tinyurl.com/2b2erkhs - Codemy.com YT channel, additional learning resources.
https://stackoverflow.com/ - troubleshooting and seeking solutions to specific programming challenges.
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
to fully execute this program, install the following extension:
(VSCode, PyCharm or other IDE's/code editiors)   # Importing modules for handling images
	1. Pillow (Python Image Preview)
	2. Tkinter (GUI)

or in console/ terminal, promt the following:
	1. pip install pillow
	2. pip install tk           # Importing the necessary modules for creating a GUI application
---------------------------------------
'''








from PIL import Image, ImageTk

original_bg_image = Image.open("bg.png")
new_width = 1200
new_height = 700  

resized_bg_image = original_bg_image.resize((new_width, new_height))
resized_bg_image.save("bg.png")
original_bg_image.close()
resized_bg_image.close()



import tkinter as tk
from tkinter import ttk, messagebox
import random
import tkinter.simpledialog



# LoginDialog class that inherits from tk.simpledialog.Dialog
class LoginDialog(tk.simpledialog.Dialog):


    def body(self, master):
        # frame to hold the content with a light background color
        frame = tk.Frame(self, bg='#feb209')
        self.configure(bg='#feb209')
        # Setting a title for the login dialog
        self.title("BeesFriend Bee Farm - Login Admin")
        # Creating and placing labels for username and password with specified properties
        ttk.Label(frame, text="Username:", background='#feb209', foreground='#333', font=("Arial", 16)).grid(row=0, pady=5)
        ttk.Label(frame, text="Password:", background='#feb209', foreground='#333', font=("Arial", 16)).grid(row=1, pady=5)
        # Creating entry widgets for username and password with specified font
        self.username_entry = ttk.Entry(frame, font=("Arial", 16))
        self.password_entry = ttk.Entry(frame, show="*", font=("Arial", 16))
        # Placing the entry widgets in the specified rows and columns
        self.username_entry.grid(row=0, column=1, pady=5)
        self.password_entry.grid(row=1, column=1, pady=5)
        # Placing the frame inside the dialog window
        frame.pack(padx=10, pady=10)
        # Returning the username_entry widget for further use
        return self.username_entry





    # Applying the input values from the entry widgets when the dialog is closed
    def apply(self):
        # Retrieving the entered values from the username and password entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Storing the retrieved values as a tuple in the 'result' attribute
        self.result = (username, password)





# Function to display the login dialog
def show_login_dialog():
    while True:
        # Creating an instance of the LoginDialog class with the main application window as the master
        dialog = LoginDialog(app)
        # Retrieving the result (username and password) from the dialog
        username, password = dialog.result
        # Checking if the entered username and password are valid
        if username == "admin" and password == "password":
            # Showing a message box with a successful login message
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            # Restoring the main application window after successful login
            app.deiconify()
            break  # Break out of the loop after successful login
        else:
            # Showing an error message box for invalid username or password
            messagebox.showerror("Login Failed", "Invalid username or password")






# Function to set up the style and background for the application window
def set_up_style_and_background(window):
    # Setting the title of the window
    window.title("BeesFriend Bee Farm Inventory")
    # Setting the background color of the window to orange
    window.configure(bg='#ffa500')
    # Disabling the ability to resize the window
    window.resizable(False, False)




# Function to calculate and display the total price of all items in the inventory
def display_total_price():
    # Reading items from the inventory
    items = read_items()
    # Calculate the total price by summing up the product of quantity and price for each item
    total_price = sum(item["quantity"] * item["price"] for item in items)
    # Update the label text with the total price in PHP
    total_price_label.config(text=f"Total Price: ₱{total_price:.2f}")



 
# CustomButton class that inherits from tk.Button
class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        # Calling the constructor of the parent class (tk.Button)
        super().__init__(master, **kwargs)
        # Storing the default background color of the button
        self.default_color = self.cget("background")
        # Setting the hover color to yellow
        self.hover_color = "#ffcc00"  # Yellow for hover
        # Binding the on_enter and on_leave methods to the mouse enter and leave events
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)



    # Method to handle the mouse enter event
    def on_enter(self, event):
        # Changing the background color to the hover color when the mouse enters the button
        self.config(background=self.hover_color)



    # Method to handle the mouse leave event
    def on_leave(self, event):
        # Restoring the default background color when the mouse leaves the button
        self.config(background=self.default_color)




# Function to generate a random product ID in the range of 1000 to 9999
def generate_product_id():
    # Using random.randint to generate a random integer between 1000 and 9999
    return random.randint(1000, 9999)




# Function to add an item with specified details to the inventory
def add_item(name, product_type, quantity, price):
    # Reading existing items from the inventory
    items = read_items()
    # Checking if the item with the same name already exists in the inventory
    for item in items:
        if item["name"] == name:
            # Displaying an error message if the item already exists
            messagebox.showerror("Error", f"Item '{name}' already exists. Please use 'Update' to modify the quantity and price.")
            return

    # Generating a new product ID
    product_id = generate_product_id()
    # Appending the new item details to the "inventory.txt" file
    with open("inventory.txt", "a") as file:
        file.write(f"{product_id},{name},{product_type},{quantity},{price}\n")
    # Displaying the updated inventory
    display_inventory()
    # Clearing the entry fields after adding the item
    clear_entries()





# Function to read items from the "inventory.txt" file and return a list of item dictionaries
def read_items():
    # Initializing an empty list to store item dictionaries
    items = []
    try:
        # Attempting to open and read the "inventory.txt" file
        with open("inventory.txt", "r") as file:
            # Iterating through each line in the file
            for line in file:
                # Stripping leading and trailing whitespaces, then splitting the line by commas
                values = line.strip().split(',')
                # Checking if there are exactly 5 values in the line
                if len(values) == 5:
                    # Unpacking the values and creating a dictionary for the item
                    product_id, name, product_type, quantity, price = values
                    items.append({
                        "product_id": int(product_id),
                        "name": name,
                        "product_type": product_type,
                        "quantity": int(quantity),
                        "price": float(price)
                    })
    # Handling the case where the file is not found
    except FileNotFoundError:
        pass
    # Returning the list of item dictionaries
    return items




# Function to update an item in the inventory based on product ID
def update_item(product_id, name, new_quantity, new_price, new_product_type):
    # Reading existing items from the inventory
    items = read_items()
    updated_items = []
    # Iterating through each item to find the one with the specified product ID
    for item in items:
        if item["product_id"] == int(product_id):
            # Updating the item details with new values
            item["name"] = name
            item["quantity"] = new_quantity
            item["price"] = new_price
            item["product_type"] = new_product_type
        updated_items.append(item)
    # Writing the updated items back to the inventory file
    write_items(updated_items)





# Function to delete multiple items from the inventory based on product IDs
def delete_multiple_items(product_ids):
    # Reading existing items from the inventory
    items = read_items()
    #  a new list with items excluding the ones to be deleted
    updated_items = [item for item in items if item["product_id"] not in product_ids]
    # Writing the updated items back to the inventory file
    write_items(updated_items)




# Function to write items to the inventory file
def write_items(items):
    # Sorting items based on product type before writing to maintain order
    sorted_items = sorted(items, key=lambda x: x['product_type'])
    # Writing sorted items to the "inventory.txt" file
    with open("inventory.txt", "w") as file:
        for item in sorted_items:
            file.write(f"{item['product_id']},{item['name']},{item['product_type']},{item['quantity']},{item['price']}\n")





# Function to display items in the inventory using a treeview widget
def display_inventory():
    # Reading items from the inventory
    items = read_items()
    # Clearing the existing items in the treeview widget
    tree.delete(*tree.get_children())
    # Inserting each item into the treeview widget
    for item in items:
        tree.insert("", "end", values=(item["product_id"], item["name"], item["product_type"], item["quantity"], item["price"]))
    # Update the total price label after displaying the updated inventory
    display_total_price()




# Function to clear all entry fields and reset the state of the product ID entry.
def clear_entries():
    # Allow modification of the product ID entry.
    product_id_entry.configure(state='normal')
    # Clear the product ID entry field.
    product_id_entry.delete(0, tk.END)
    # Make the product ID entry read-only again.
    product_id_entry.configure(state='readonly')
    # Clear the name entry field.
    name_entry.delete(0, tk.END)
    # Set the product type combobox to an empty string.
    product_type_combobox.set('')
    # Clear the quantity entry field.
    quantity_entry.delete(0, tk.END)
    # Clear the price entry field.
    price_entry.delete(0, tk.END)



# Function to handle the selection of an item in the treeview widget
def on_item_select(event):
    # Getting the selected item from the treeview widget
    selected_item = tree.selection()
   # Check if an item is selected in the treeview
    if selected_item:
        # Extract values from the selected item and populate entry fields
        # Get values associated with the selected item
        item = tree.item(selected_item, 'values')

        # Allow modification of the product ID entry.
        product_id_entry.configure(state='normal')
        # Clear the product ID entry field.
        product_id_entry.delete(0, tk.END)
        # Insert the product ID value into the product ID entry.
        product_id_entry.insert(0, item[0])
        # Make the product ID entry read-only again.
        product_id_entry.configure(state='readonly')


        # Clear the name entry field.
        name_entry.delete(0, tk.END)
        # Insert the name value into the name entry.
        name_entry.insert(0, item[1])


        # Set the product type combobox to the selected product type.
        product_type_combobox.set(item[2])
        # Clear the quantity entry field.
        quantity_entry.delete(0, tk.END)
        # Insert the quantity value into the quantity entry.
        quantity_entry.insert(0, item[3])
        # Clear the price entry field.
        price_entry.delete(0, tk.END)
        # Insert the price value into the price entry.
        price_entry.insert(0, item[4])
    else:
        # Clearing entry fields if no item is selected
        clear_entries()





# Function to handle the click event of the "Add" button
def add_button_click():
    # Retrieve values from entry fields
    # Get the name value from the name entry.
    name = name_entry.get()
    # Get the selected product type from the product type combobox.
    product_type = product_type_combobox.get()
    # Get the quantity value from the quantity entry.
    quantity = quantity_entry.get()
    # Get the price value from the price entry.
    price = price_entry.get()

    # Checking if all fields are filled
    if name and product_type and quantity and price:
        try:
            # Converting quantity and price to integers and float, respectively
            quantity = int(quantity)
            price = float(price)
            # Adding the item to the inventory
            add_item(name, product_type, quantity, price)
            # Displaying the updated inventory
            display_inventory()
        except ValueError:
            # Showing an error message for invalid quantity or price
            messagebox.showerror("Error", "Invalid quantity or price. Please enter numeric values.")
    else:
        # Showing an error message for unfilled fields
        messagebox.showerror("Error", "All fields must be filled.")
    clear_entries()





# Function to handle the click event of the "Update" button
def update_button_click():
    # Getting the selected item from the treeview widget
    selected_item = tree.selection()
    if selected_item:
        # Get the product ID value from the product ID entry.
        product_id = product_id_entry.get()
        # Get the name value from the name entry.
        name = name_entry.get()
        # Get the new quantity value from the quantity entry.
        new_quantity = quantity_entry.get()
        # Get the new price value from the price entry.
        new_price = price_entry.get()
        # Get the new product type from the product type combobox.
        new_product_type = product_type_combobox.get()
        # Checking if all required fields are filled
        if product_id and name and new_quantity and new_price:
            try:
                # Convert the product ID value to an integer.
                product_id = int(product_id)
                # Convert the new quantity value to an integer.
                new_quantity = int(new_quantity)
                # Convert the new price value to a float.
                new_price = float(new_price)
                # Updating the item in the inventory
                update_item(product_id, name, new_quantity, new_price, new_product_type)
                # Displaying the updated inventory
                display_inventory()
            except ValueError:
                # Showing an error message for invalid product ID, quantity, or price
                messagebox.showerror("Error", "Invalid product ID, quantity, or price. Please enter numeric values.")
        else:
            # Showing an error message for unfilled fields
            messagebox.showerror("Error", "All fields must be filled.")
    else:
        # Showing an error message if no item is selected
        messagebox.showerror("Error", "Please select an item to update.")
    clear_entries()





# Function to handle the click event of the "Delete Selected" button
def delete_selected_button_click():
    # Getting the selected items from the treeview widget
    selected_items = tree.selection()
    if selected_items:
        # Extracting product IDs from the selected items
        product_ids = [int(tree.item(item, 'values')[0]) for item in selected_items]
        # Deleting the selected items from the inventory
        delete_multiple_items(product_ids)
        # Displaying the updated inventory
        display_inventory()
    else:
        # Showing an error message if no item is selected
        messagebox.showerror("Error", "Please select items to delete.")
    clear_entries()





# Function to search for a product by ID
def search_product():
    # Getting the search ID from the entry field
    search_id = search_entry.get().strip()
    if search_id:
        try:
            # Converting search ID to an integer
            search_id = int(search_id)
            found = False
            # Iterating through items in the treeview widget
            for item in tree.get_children():
                # Extracting values from the item
                values = [int(value) if value.isdigit() else value for value in tree.item(item, 'values')]
                # Checking if the search ID matches the product ID in the item
                if values and values[0] == search_id:
                    # Selecting and focusing on the found item in the treeview
                    tree.selection_set(item)
                    #    Set the focus on the matched item.
                    tree.focus(item)
                    #    Set 'found' to True to indicate that a match has been found.
                    found = True
                    #   Exit the loop to stop further searching.
                    break
            # Showing a message if the search ID is not found
            if not found:
                messagebox.showinfo("Search", f"Product ID {search_id} not found.")
        except ValueError:
            # Showing an error message for an invalid search ID
            messagebox.showerror("Error", "Invalid Product ID. Please enter a numeric value.")
    else:
        # Showing a warning message for an empty search ID
        messagebox.showwarning("Warning", "Please enter a Product ID for search.")






# GUI setup
app = tk.Tk()
app.title("BeesFriend Bee Farm Inventory")
app.configure(bg='#ffa500')  # Set the background color of the main window
app.resizable(False, False)  # Disable window resizing
# Set icon for the main window
main_window_icon = Image.open("logo.png")
main_window_icon_photo = ImageTk.PhotoImage(main_window_icon)
app.iconphoto(True, main_window_icon_photo)


# Background image
background_image = Image.open("bg.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


total_price_label = ttk.Label(app, text="Total Price: ₱0.00", background='yellow', font=("Arial", 16))
total_price_label.grid(row=4, column=3, columnspan=2, padx=10, pady=5)



# Labels and entry fields for Product ID, Item Name, Product Type, Quantity, and Price
product_id_label = ttk.Label(app, text="Product ID:", background='#feb209', font=("Arial", 16))
product_id_label.grid(row=0, column=0, padx=10, pady=5)
product_id_entry = ttk.Entry(app, state="readonly", font=("Arial", 16))
product_id_entry.grid(row=0, column=1, padx=10, pady=5)

search_label = ttk.Label(app, text="Search by Product ID:", background='#feb209', font=("Arial", 16))
search_label.grid(row=0, column=2, padx=10, pady=5)
search_entry = ttk.Entry(app, font=("Arial", 16))
search_entry.grid(row=0, column=3, padx=10, pady=5)

search_button = CustomButton(app, text="Search", command=search_product, background="yellow", relief="flat", font=("Arial", 16))
search_button.grid(row=0, column=4, pady=5)

name_label = ttk.Label(app, text="Item Name:", background='#feb209', font=("Arial", 16))
name_label.grid(row=1, column=0, padx=10, pady=5)
name_entry = ttk.Entry(app, font=("Arial", 16))
name_entry.grid(row=1, column=1, padx=10, pady=5)

product_type_label = ttk.Label(app, text="Product Type:", background='#feb209', font=("Arial", 16))
product_type_label.grid(row=2, column=0, padx=10, pady=5)
product_types = ["Bee Pollen", "Bee Propolis", "Pure Honey", "Assorted", "Beauty products"]
product_type_combobox = ttk.Combobox(app, values=product_types, font=("Arial", 16))
product_type_combobox.grid(row=2, column=1, padx=10, pady=5)

quantity_label = ttk.Label(app, text="Quantity:", background='#feb209', font=("Arial", 16))
quantity_label.grid(row=3, column=0, padx=10, pady=5)
quantity_entry = ttk.Entry(app, font=("Arial", 16))
quantity_entry.grid(row=3, column=1, padx=10, pady=5)

price_label = ttk.Label(app, text="Price:", background='#feb209', font=("Arial", 16))
price_label.grid(row=4, column=0, padx=10, pady=5)
price_entry = ttk.Entry(app, font=("Arial", 16))
price_entry.grid(row=4, column=1, padx=10, pady=5)

# Treeview widget to display the inventory
tree = ttk.Treeview(app, columns=("Product ID", "Name", "Product Type", "Quantity", "Price"), show="headings")
tree.heading("Product ID", text="Product ID", anchor=tk.CENTER)
tree.heading("Name", text="Name", anchor=tk.CENTER)
tree.heading("Product Type", text="Product Type", anchor=tk.CENTER)
tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)
tree.heading("Price", text="Price", anchor=tk.CENTER)
tree.grid(row=5, column=0, columnspan=5, pady=10)
# Create a vertical scroll bar for the treeview
scrollbar = ttk.Scrollbar(app, orient="vertical", command=tree.yview)
scrollbar.grid(row=5, column=5, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)
# Bind the Treeview select event to the on_item_select function
tree.bind("<<TreeviewSelect>>", on_item_select)
# Style configuration for custom button
style = ttk.Style()
style.configure("Yellow.TButton", foreground="black", borderwidth=0, relief="flat")
# Custom button for adding a new item to the inventory
add_button = CustomButton(app, text="Add", command=add_button_click, background="yellow", relief="flat", font=("Arial", 16))
add_button.grid(row=6, column=0, pady=5)
# Custom button for updating an existing item in the inventory
update_button = CustomButton(app, text="Update", command=update_button_click, background="yellow", relief="flat", font=("Arial", 16))
update_button.grid(row=6, column=1, pady=5)
# Custom button for clearing all entry fields
clear_button = CustomButton(app, text="Clear All", command=clear_entries, background="yellow", relief="flat", font=("Arial", 16))
clear_button.grid(row=6, column=3, pady=5)
# Custom button for deleting selected items from the inventory
delete_selected_button = CustomButton(app, text="Delete Selected", command=delete_selected_button_click, background="yellow", relief="flat", font=("Arial", 16))
delete_selected_button.grid(row=6, column=2, pady=5)











display_inventory()
# 
display_total_price()
# Minimize the application window initially
app.iconify()
# Show the login dialog and wait for successful login
show_login_dialog()
# Start the main event loop to run the application
app.mainloop()

