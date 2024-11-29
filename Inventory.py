#This project acknowledges the use of LLM to assist in the creation of the GUI
import os

class Inventory:

    inventorylst = []

    def __init__(self, itemName, itemQnty):
        self.itemName = itemName
        self.itemQnty = itemQnty
        Inventory.inventorylst.append(self) # this will add the item to the long standing list of inventory items
        self.save_inventory_to_file()

    def save_inventory_to_file(self):
        with open("inventory.txt", "w") as file:
            for item in Inventory.inventorylst:
                inventory_info = f"Item: {item.itemName}, Quantity: {item.itemQnty}"
                file.write(f"{inventory_info}\n")
                break

    def display_inventory():
        for item in Inventory.inventorylst:
            (f"Item: {item.itemName}, Quantity:{item.itemQnty}")

    def update_inventory(name,itemqnty):# this is to directly change and set the amount, eg after restocking changing from 2 eggs to 12
        for item in Inventory.inventorylst:
            if item.itemName == name:                
                item.itemQnty = itemqnty
                item.save_inventory_to_file()
                break
    
    def addInventory(ingredient,quantity):
         # the other things liek inventory and order would have the same format to add stuff, the owner, manager and such would be the people that have access to these functions 
        
        Inventory.inventorylst.append(Inventory(ingredient,quantity))
        Inventory.inventorylst[-1].save_inventory_to_file()
    
    def findInventory(name):
        
        output = []
        for item in Inventory.inventorylst:
            if item.itemName == name:
                return item.itemName
        
        

                
    def updateInvAuto(itemName,itemQuan):

        for item in Inventory.inventorylst:
            if item.itemName == itemName:
                
                item.itemQnty = item.itemQnty - itemQuan # so this will subtract the amout of a particular ingredient that would be used to fill an order from the existing amount; therfore updating/keeping track of amount of ingredients left
                item.save_inventory_to_file()
                break