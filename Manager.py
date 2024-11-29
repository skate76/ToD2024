#This project acknowledges the use of LLM to assist in the creation of the GUI
import tkinter as tk
from tkinter import messagebox
from Employee import EmployeeApp
from Employee import EmployeeMng
from Recipe import Recipe
from Recipe import RecipeApp
from Employee import Employee
from Inventory import Inventory
import tkinter.simpledialog as simpledialog


class Manager:
    def __init__(self):
        self.inventory = Inventory.inventorylst
        self.employee_list = Employee.employee_list
        
        self.window = tk.Tk()
        self.window.title("Manager Dashboard")
        
        
        self.create_buttons()

    def create_buttons(self):
        
        self.inventory_button = tk.Button(self.window, text="Add/Update Inventory", command=self.inventory_mgmt)
        self.inventory_button.pack(pady=10)

        
        self.reports_button = tk.Button(self.window, text="Generate Reports", command=self.generate_reports)
        self.reports_button.pack(pady=10)

        
        self.manage_staff_button = tk.Button(self.window, text="Manage Staff", command=self.manage_staff)
        self.manage_staff_button.pack(pady=10)

        



        # Exit Button
        self.exit_button = tk.Button(self.window, text="Exit", command=self.window.quit)
        self.exit_button.pack(pady=10)

    def inventory_mgmt(self):
      
        self.new_window("Inventory Management", [
            ("Display Inventory", self.display_inventory),
            ("Add New Inventory", self.add_inventory),
            ("Update Inventory", self.update_inventory),
            ("Back", self.close_window)
        ])

    
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

    #def remove_inventory(self):
        #item_name = self.ask_input("Enter item name to remove: ")
        #if item_name is None:
            #return  
    
        
        #item = Inventory.findInventory(item_name)
        #if item is None:
            #messagebox.showerror("Error", "Item Not Found.")
            #return
    
        # Remove the item
        #self.inventory.remove(item_name)
        #messagebox.showinfo("Success", f"Item '{item_name}' removed successfully!")

    
    def generate_reports(self):
        # Repo logic
        messagebox.showinfo("Reports", "Reports generated successfully!")

    def manage_staff(self):
        Employee.load_employees()
        
        root = tk.Tk()
        EmployeeMng(root)
        # Staff management window
        #self.new_window("Manage Staff", [
            #("Display All Staff", self.display_all_staff),
            #("Add Staff", self.add_staff),
            #("Update Staff", self.update_staff),
            #("Remove Staff", self.remove_staff),
            #("Back", self.close_window)
        #])

    def display_all_staff(self):
        
        if Employee.employee_list:
            staff_info = "\n".join([f"ID: {emp.employee_id}, Name: {emp.employee_name}, Position: {emp.position}, Phone: {emp.phone_number}, Email: {emp.email}" for emp in Employee.employee_list])
            messagebox.showinfo("Employee List", f"Staff Members:\n{staff_info}")
        else:
            messagebox.showinfo("Employee List", "No employees found.")


    def add_staff(self):
        employee_id = int(self.ask_input("Enter Employee ID: "))
        employee_name = self.ask_input("Enter employee name: ")
        employee_position = self.ask_input("Enter employee position: ")
        username = self.ask_input("Enter username: ")
        password = self.ask_input("Enter password: ")
        phone_number = self.ask_input("Enter phone number: ")
        email = self.ask_input("Enter email: ")
        status = self.ask_input("Enter status (Active/Inactive): ") or "Active"
    
        # Create a new Employee object with the correct number of arguments
        new_employee = Employee(employee_id, employee_name, employee_position, username, password, status, phone_number, email)
        messagebox.showinfo("Success", f"Employee {employee_name} added successfully!")

        
        new_employee = Employee(employee_id, employee_name, employee_position, username, password, phone_number, email, status)
        messagebox.showinfo("Success", f"Employee {employee_name} added successfully!")

    def update_staff(self):
        employee_id = int(self.ask_input("Enter Employee ID to update: "))
    
        #Trying to find the employee using the employee_finder method
        employee = Employee.employee_finder(employee_id)  # Correctly using the class method
    
        if employee:
         #Employee found
            new_phone = self.ask_input(f"Enter new phone number (Current: {employee.phone_number}): ")
            new_email = self.ask_input(f"Enter new email (Current: {employee.email}): ")
            employee.phone_number = new_phone
            employee.email = new_email
            messagebox.showinfo("Success", f"Staff member {employee.employee_name}'s details updated successfully!")
        else:
            # Employee not found, show error
            messagebox.showerror("Error", "Employee not found.")

    def remove_staff(self):
    #Ask for employee ID to remove
        employee_id = int(self.ask_input("Enter Employee ID to remove: "))
    
    
        employee = Employee.employee_finder(employee_id) 
    
        if employee:
            Employee.employee_list.remove(employee)
            messagebox.showinfo("Success", f"Employee {employee.employee_name} removed successfully!")
        else:
            messagebox.showerror("Error", "Employee not found.")


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
    manager = Manager()
    manager.run()