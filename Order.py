#This project acknowledges the use of LLM to assist in the creation of the GUI
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
        self.name = custName
        self.phone = custPNum
        self.item = dessert #from recipe class
        self.orderDetails = Recipe.findRecipe(dessert)
        #self.allergy = allergy # should be serperated my commas; if none then NONE would be writen down instead 
        self.status = "Pending" # This is always the default status when a order is made
        Order.orderslst.append(self)

        #self.window = tk.Tk()
        #self.window.title("Order Dashboard")

        #Order.orderApp()
        #self.orderConfirm()

    def update_order(cls,custName,dessert):# this is to directly change and set the amount, eg after restocking changing from 2 eggs to 12
        for od in Order.orderslst:
            if od.name == custName:                
                od.item = dessert
                cls.save_orders()
                break
        

    #def orderConfirm(cls):

        #print(self.orderDetails)
        #for item,quan in self.orderDetails:
        #    print(item,quan)
            
            
        #    Inventory.updateInvAuto(item,quan)# item name in idex 0 and item quantity in index 1

        #self.orderNum = self.orderNum + 1
        #Order.orderslst.append(self) #or just append the class itself
        #Order.save_orders()

        #print("Order has been Confirmed!")
    
    @classmethod
    def load_orders(cls):
        try:
            with open("orders.txt", "r") as file:
                for line in file:
                    details = line.strip().split(", ")

                    if len(details) >= 4:  
                        custName = details[0].split(": ")[1]
                        custPNum = details[1].split(": ")[1]
                        dessert = details[2].split(": ")[1]
                        status = details[3].split(": ")[1]
                        # Creating Order object
                        Order(custName, custPNum, dessert)
        except FileNotFoundError:
            print("No order file found. Creating a new one.")
        #    cls.order_initialization()

    @classmethod
    def save_orders(cls):
        with open("orders.txt", "w") as file:
            for od in cls.orderslst:
                file.write(f"Customer Name: {od.name}, Phone Number: {od.phone}, Dessert: {od.item}, Status: {od.status} \n")

   
    

    def manage_orderStatus(self,name,status):
        for od in Order.orderslst:
            if od.name == name:                
                od.status = status
                Order.save_orders()
                break

    

        

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

        
        tk.Label(root, text="Customer Phone Number:").pack(pady=5)
        self.cust_phone_entry = tk.Entry(root)
        self.cust_phone_entry.pack(pady=5)

        
        tk.Label(root, text="Dessert Name:").pack(pady=5)
        self.dessert_entry = tk.Entry(root)
        self.dessert_entry.pack(pady=5)

        
        tk.Button(root, text="Place Order", command=self.place_order).pack(pady=20)

        
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
            


        #Create the Order object
        new_order = Order(cust_name, cust_phone, dessert)
        
        #Display order confirmation
        self.order_status.delete(1.0, tk.END)
        self.order_status.insert(tk.END, f"Order placed successfully!\nOrder Number: {new_order.orderNum}\nCustomer: {cust_name}\nDessert: {dessert}\nStatus: {new_order.status}\n")
        Order.save_orders()

    


    @classmethod
    def display_orders(cls):
        orders = "\n".join([f"Order {order.orderNum}: {order.custName} - {order.dessert} - Status: {order.status}" for order in cls.orderslst])
        return orders

# Main program execution
if __name__ == "__main__":
    Order.load_orders()  # Load employees from the file at the start
    root = tk.Tk()
    app = OrderApp(root)
    root.mainloop()