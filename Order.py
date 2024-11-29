from Recipe import Recipe
from Inventory import Inventory
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Order:

   orderslst=[]
   orderNum = 10001

   

   def __init__(self, custName, custPNum,dessert):
        self.custName = custName
        self.custPNum = custPNum
        self.dessert = dessert #from recipe classNEED TO MAKE RECIPE CLASS
        self.orderDetails = Recipe.findRecipe(dessert)
        #self.allergy = allergy # should be serperated my commas; if none then NONE would be writen down instead 
        self.status = "Pending" # This is always the default status when a order is made

        self.window = tk.Tk()
        self.window.title("Order Dashboard")

        #Order.orderApp()
        self.orderConfirm()
        

   def orderConfirm(self):

        
        print(self.orderDetails)
        for item,quan in self.orderDetails:
            print(item,quan)
            
            
            Inventory.updateInvAuto(item,quan)# item name in idex 0 and item quantity in index 1

        self.orderNum = self.orderNum + 1
        Order.orderslst.append(self) #or just append the class itself
        print("Order has been Confirmed!")
    


   
    

   def manage_orderStatus(self):
        status = (input("Enter wether you would like to change the selected order status to Started or Completed"))
        # if possible this could be a dropdown thing
        self.status = status

class OrderApp:
    
    orderslst = []
    orderNum = 10001

    def __init__(self, root):
        self.root = root
        self.root.title("Order Management System")

        # Customer Name
        tk.Label(root, text="Customer Name:").pack(pady=5)
        self.cust_name_entry = tk.Entry(root)
        self.cust_name_entry.pack(pady=5)

        # Customer Phone Number
        tk.Label(root, text="Customer Phone Number:").pack(pady=5)
        self.cust_phone_entry = tk.Entry(root)
        self.cust_phone_entry.pack(pady=5)

        # Dessert Name
        tk.Label(root, text="Dessert Name:").pack(pady=5)
        self.dessert_entry = tk.Entry(root)
        self.dessert_entry.pack(pady=5)

        # Order Button
        tk.Button(root, text="Place Order", command=self.place_order).pack(pady=20)

        # Display area for order confirmation
        self.order_status = tk.Text(root, height=10, width=50)
        self.order_status.pack(pady=20)

    def place_order(self):
        # Get the entered values
        cust_name = self.cust_name_entry.get()
        cust_phone = self.cust_phone_entry.get()
        dessert = self.dessert_entry.get()

        if not cust_name or not cust_phone or not dessert:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        if Recipe.findRecipe(dessert) is None:
            messagebox.showerror("Error", "We do not offer this dessert.")
            return
            


        # Create the Order object
        new_order = Order(cust_name, cust_phone, dessert)
        
        # Display order confirmation
        self.order_status.delete(1.0, tk.END)
        self.order_status.insert(tk.END, f"Order placed successfully!\nOrder Number: {new_order.orderNum}\nCustomer: {cust_name}\nDessert: {dessert}\nStatus: {new_order.status}\n")

    @classmethod
    def display_orders(cls):
        orders = "\n".join([f"Order {order.orderNum}: {order.custName} - {order.dessert} - Status: {order.status}" for order in cls.orderslst])
        return orders

# Main program execution


    

    

    