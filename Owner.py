import tkinter as tk
from tkinter import messagebox
from Employee import Employee

from Inventory import Inventory
from Manager import Manager
from Recipe import RecipeApp
import tkinter.simpledialog as simpledialog

class Owner:
    def __init__(self):
        Employee.load_employees()
        self.employee_list = Employee.employee_list
        
        self.window = tk.Tk()
        self.window.title("Owner Dashboard")
        
        #buttons!
        self.create_buttons()

    def create_buttons(self):
        #button definitions
        # Add/Update Inventory Button
        self.inventory_button = tk.Button(self.window, text="Add/Update Inventory", command=self.inventory_mgmt)
        self.inventory_button.pack(pady=10)

        # Generate Payroll Button
        self.payroll_button = tk.Button(self.window, text="Generate Payroll", command=self.generatePayroll)
        self.payroll_button.pack(pady=10)

        # Manage Recipe Button
       # self.recipes_button = tk.Button(self.window, text="Manage Recipes", command=self.manageRecipe)
      #  self.recipes_button.pack(pady=10)

        # Manage Orders Button
      #  self.orders_button = tk.Button(self.window, text="Manage Orders", command=self.manageOrders)
      #  self.orders_button.pack(pady=10)
        
        # Manage Staff Button
        self.manageEmp_button = tk.Button(self.window, text="Manage Staff", command=Manager.manage_staff)
        self.manageEmp_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self.window, text="Exit", command=self.window.quit)
        self.exit_button.pack(pady=10)


    def generatePayroll(self):
    #Opens inventory management window
        self.new_window("Payroll Generator", [
            ("Generate Employee Payroll", self.genProll),
            ("Back", self.close_window)
        ])

    def genProll(self):
        if self.employee_list:
            paylist = ""
            for e in self.employee_list:
                paylist += (
                    f"ID: {e.employee_id}\n"
                    f"Name: {e.employee_name}\n"
                    f"Position: {e.position}\n"
                    f"Pay: {e.payrate*e.hours_worked}\n"
                    f"\n"
                    f"\n"
                )
        messagebox.showinfo("Payroll generated successfully!", paylist)
        
    def inventory_mgmt(self):
        #Opens inventory management window
        self.new_window("Inventory Management", [
            ("Display Inventory", self.display_inventory),
            ("Add New Inventory", self.add_inventory),
            ("Update Inventory", self.update_inventory),
            ("Back", self.close_window)
        ])

    #def display_inventory(self):
        #inventory_info = "\n".join([f"Item: {item.itemName}, Quantity: {item.itemQnty}" for item in Inventory.inventorylst])
        #messagebox.showinfo("Inventory", f"Current Inventory:\n{inventory_info}")

    def display_inventory(self):
        for item in Inventory.inventorylst:
            inventory_info = f"Item: {item.itemName}, Quantity: {item.itemQnty}" 
            messagebox.showinfo("Inventory", f"Current Inventory:\n{inventory_info}")
            break

    def add_inventory(self):
        item_name = self.ask_input("Enter item name: ")
        if item_name is None:
            return  
        
        item_qnty = self.ask_input("Enter quantity: ", int)
        if item_qnty is None:
            return  
        
        Inventory.addInventory(item_name, item_qnty)
        messagebox.showinfo("Success", f"Item '{item_name}' added successfully!")

    def update_inventory(self):
        item_name = self.ask_input("Enter item name to update: ")
        if item_name is None:
            return  
    
        #find
        item = Inventory.findInventory(item_name)
        if item is None:
            messagebox.showerror("Error", "Item Not Found.")
            return

        #new quant
        new_qnty = self.ask_input(f"Enter new quantity for {item_name}: ", int)
        if new_qnty is None:
            return  
    
        Inventory.update_inventory(item_name,new_qnty)
        messagebox.showinfo("Success", f"Quantity for '{item_name}' updated to {new_qnty}.")

    #Inventory.load_inventory_from_file()

    #def display_inventory(self):
        #inventory_info = "\n".join([f"Item: {item.itemName}, Quantity: {item.itemQnty}" for item in Inventory.inventorylst])
        #messagebox.showinfo("Inventory", f"Current Inventory:\n{inventory_info}")

    
    def display_inventory(self):
        if not Inventory.inventorylst:
            messagebox.showinfo("Inventory", f"No items are registered")
            return
        
        inventory_info = "\n".join([f"Item: {item.itemName}, Quantity: {item.itemQnty}" for item in Inventory.inventorylst])
        messagebox.showinfo("Inventory", f"Current Inventory:\n{inventory_info}")
        pass
            

    def add_inventory(self):
        item_name = self.ask_input("Enter item name: ")
        if item_name is None:
            return  
        
        item_qnty = self.ask_input("Enter quantity: ", int)
        if item_qnty is None:
            return  
        
        Inventory.addInventory(item_name, item_qnty)
        messagebox.showinfo("Success", f"Item '{item_name}' added successfully!")

    
    def update_inventory(self):
        item_name = self.ask_input("Enter item name to update: ")
        if item_name is None:
            return  
    
        #find
        item = Inventory.findInventory(item_name)
        if item is None:
            messagebox.showerror("Error", "Item Not Found.")
            return

        #new quant
        new_qnty = self.ask_input(f"Enter new quantity for {item_name}: ", int)
        if new_qnty is None:
            return  
    
        Inventory.update_inventory(item_name,new_qnty)
        messagebox.showinfo("Success", f"Quantity for '{item_name}' updated to {new_qnty}.")
        
    def manageRecipe(self):
    #Opens inventory management window
        self.new_window("Recipe Manager", [
            ("Adjust recipes", self.recpManage),
            ("Back", self.close_window)
        ])

    def recpManage(self):
        return 0


    def ask_input(self, prompt, cast_type=str):
        user_input = simpledialog.askstring("Input", prompt)
        if user_input is None or user_input == "":
            return None  
        
        try:
            return cast_type(user_input)  
        except ValueError:
            messagebox.showerror("Invalid Input", f"Please enter a valid {cast_type.__name__}.")
            return None

    def close_window(self):
        #loses the current window and returns to the main window
        self.window.deiconify()

    def new_window(self, title, button_info):
        """Create a new window with specific buttons"""
        new_win = tk.Toplevel(self.window)
        new_win.title(title)

        for text, cmd in button_info:
            button = tk.Button(new_win, text=text, command=cmd)
            button.pack(pady=10)
        
        # Hides the main window
        self.window.withdraw()

        new_win.protocol("WM_DELETE_WINDOW", self.close_window)  # Handle close event

    def run(self):
        #gui
        self.window.mainloop()


if __name__ == "__main__":
    owner = Owner()
    owner.run()
