import getpass
import os
import tkinter as tk
from Employee import EmployeeApp
from Recipe import RecipeApp
from Manager import Manager
from Order import OrderApp

Musernames = ["manager123"]
Mpasswords = ["manager123"]

Eusernames = ["employee123"]
Epasswords = ["employee123"]

Ousernames = ["KTAIT123"]
Opasswords = ["KTAIT123"]

inventory = [["cakes", 10],["cookies",10]]

#def login():
    #while True:
       # print("Welcome! Please log in.")
        #username = input("Please enter your username: ")
        #password = getpass.getpass("Please enter your password")
       # if ((username in Eusernames) and (password in Epasswords)):
           # emp_menu()
        #elif ((username in Cusernames) and (password in Cpasswords)):
           # cus_menu()
       # elif ((username in Ousernames) and (password in Opasswords)):
            #admin_menu()
        #else:
           # print("INVALID PASSWORD")
           # print('')
           # print("please try again")
          #  os.system('cls')
           # login()
           # pass




def admin_menu():
    #import tkinter as tk    this needs to be at the top of your file...
    #thats just about all we need to make the buttons work..

    root = tk.Tk() ##creates window
    root.title("Admin Menu") #name of window
        

        #here, instead of having inputs, youd have buttons

    button = tk.Button(root, text = "Add/Update Inventory", command=inventory_mgmt) #command is the function called when button is clicked
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Generate Reports", command=generate_reports)
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Manage Staff", command=staff_mgmt)
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Exit")
    button.pack(padx=20, pady= 20)

        
        #print("1. Add/Update Inventory")
        #print("2. Generate Reports")
        #print("3. Manage Staff")
        #print("4. Exit")
    #choice = int(input("Please Select A Function:"))
    
    #if choice == 1:
       # print ("Add/Update Inventory")
        #os.system('cls')
        #inventory_mgmt()
    #elif choice == 2:
        #print("Manage Staff")
        #os.system('cls')
        #staff_mgmt()
    #elif choice == 3:
        #print("Generate Reports")
        #os.system('cls')
        #generate_reports()
    #elif choice == 4:
        #print("Exiting......")
        #os.system('cls')
        #break 
    #else:
        #print("Invalid Choice. Please enter a number from 1 - 4")
        #os.system('cls')
        #admin_menu()
        
        
def cus_menu():
        
    root = tk.Tk()
    root.title("Customer Menu")


    button = tk.Button(root, text = "Make an Order", command=make_order)
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Display Inventory", command=display)
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Exit")
    button.pack(padx=20, pady= 20)



    #while True:
        #print("1. Make an Order")
        #print("2. Display Inventory")
        #print("3. Exit")
     

        #choice = int(input("Please Select A Function:"))
        #if choice == 1:
            #print ("Make an Order")
            #os.system('cls')
            #make_order()
        #elif choice == 2:
            #print("Display Inventory")
            #os.system('cls')
            #display()
            
        #elif choice == 3:
            #print("Exiting....")
            #os.system('cls')
            #break
        #else:
            #print("Invalid Choice. Please enter a number from 1 - 3")
            #os.system('cls')
            #cus_menu()
        


def emp_menu():
    root = tk.Tk()
    root.title("Employee Menu")

    button = tk.Button(root, text = "Add/Update Inventory", command=inventory_mgmt)
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Check in/Check out", command=chekin_menu)
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Exit")
    button.pack(padx=20, pady= 20)
    
    #print("1. Add/Update Inventory")
    #print("2. Check in/Check out")
    #print("3. Exit")
    
    #choice = int(input("Please Select A Function:"))
    #if choice == 1:
        #print ("Add/Update Inventory")
        #os.system('cls')
        #inventory_mgmt()
        
    #elif choice == 2:
       # print("Check in/Check out")
        #os.system('cls')
        #chekin_menu()
       # os.system('cls')
   # elif choice == 3:
        #print("Exiting....")
        #os.system('cls')
        #break
    #else:
       # print("Invalid Choice. Please enter a number from 1 - 3")
       # os.system('cls')
        #emp_menu()




def inventory_mgmt():
    
        #print("Welcome to the Inventory Manager")
        #print('')
        #print("1. Display inventory")
        #print("2. Add New inventory")
        #print("3. Update inventory")
        #print("4. Remove inventory")
        #print("5. Go Back")
        root = tk.Tk()
        root.title("INVENTORY")

        #choice = int(input("Please Select A Function:"))
        button = tk.Button(root, text = "Display", command=display)
        button.pack(padx=20, pady= 20)

        button = tk.Button(root, text = "Add Inventory", command=add_inventory)
        button.pack(padx=20, pady= 20)

        button = tk.Button(root, text = "Update Inventory", command=update_inventory)
        button.pack(padx=20, pady= 20)

        button = tk.Button(root, text = "Remove Inventory", command=remove_inventory)
        button.pack(padx=20, pady= 20)

        button = tk.Button(root, text = "Go Back")
        button.pack(padx=20, pady= 20)


        #if choice == 1:
            #print ("Display")
            #os.system('cls')
            #display()
            #break
        #elif choice == 2:
            #print("Add Inventory")
            #os.system('cls')
            #add_inventory()
        #elif choice == 3:
            #print("Update Inventory")
            #os.system('cls')
            #update_inventory()
        #elif choice == 4:
            #print("Remove Inventory")
            #os.system('cls')
            #remove_inventory()
        #elif choice == 5:
            #print("Exiting....")
            #os.system('cls')
            #break
        #else:
           # print("Invalid Choice. Please enter a number from 1 - 5")
            #os.system('cls')
            #inventory_mgmt()
        

        
    

def add_inventory():
    root = tk.Tk()
    root.title("ADD INVENTORY")
    print("Welcome to the Inventory Manager")

def update_inventory():
    root = tk.Tk()
    root.title("UPDATE INVENTORY")
    print("Welcome to the Inventory Manager")

def remove_inventory():
    root = tk.Tk()
    root.title("REMOVE INVENTORY")
    print("Welcome to the Inventory Manager")

def display():
    print("")
    for i in inventory:
        print (i)
        print('')


def chekin_menu():
    root = tk.Tk()
    root.title("CHECKIN MENU")
    while True:
        print("1. Checkin")
        print("2. Checkout")
        print("3. Exit")
     

        choice = int(input("Please Select A Function:"))
        if choice == 1:
            print ("Check in")
            os.system('cls')
            checkin()
        elif choice == 2:
            print("Checkout")
            os.system('cls')
            checkout()
            
        elif choice == 3:
            print("Exiting....")
            os.system('cls')
            break
        else:
            print("Invalid Choice. Please enter a number from 1 - 3")
            os.system('cls')
            chekin_menu()

def checkin():
    root = tk.Tk()
    root.title("CHECKIN")
    print("Welcome to the Inventory Manager")

def checkout():
    root = tk.Tk()
    root.title("CHECKOUT")
    print("Welcome to the Inventory Manager")




def staff_mgmt():
    root = tk.Tk()
    root.title("STAFFMANAGER")


    button = tk.Button(root, text = "Add Staff", command=add_staff)
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Update Staff", command=update_staff)
    button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "REmove Staff", command=remove_staff)
    button.pack(padx=20, pady= 20)

    #button = tk.Button(root, text = "Remove Inventory", command=remove_inventory)
    #button.pack(padx=20, pady= 20)

    button = tk.Button(root, text = "Go Back")
    button.pack(padx=20, pady= 20)
    
        

def add_staff():
    root = tk.Tk()
    root.title("ADD STAFF")
    print("Welcome to the Inventory Manager")

def remove_staff():
    root = tk.Tk()
    root.title("rEMOVE STAFF")
    print("Welcome to the Inventory Manager")

def update_staff():
    root = tk.Tk()
    root.title("UPDATE STAFF")
    print("Welcome to the Inventory Manager")



def generate_reports():
    root = tk.Tk()
    root.title("HENERATE REPORTS")

    print("Welcome to the Inventory Manager")




def make_order():
    root = tk.Tk()
    root.title("MAKE ORDER")
    print("Welcome to the Inventory Manager")




def quit():
    global root
    root.quit()

def Login():
    username = username_entry.get()
    password = password_entry.get()
    if ((username in Eusernames) and (password in Epasswords)):
            #emp_menu()
            login_window.destroy()
            root = tk.Tk()

            print("1")
            
            app = EmployeeApp(root)
            root.mainloop()



    elif ((username in Musernames) and (password in Mpasswords)):
            #cus_menu()
            login_window.destroy()
            root = tk.Tk()

            print("2")
            
            app = Manager()
            root.mainloop()
            root.destroy()
    elif ((username in Ousernames) and (password in Opasswords)):
            login_window.destroy()
            root = tk.Tk()

            print("2")
            
            app = OrderApp(root)
            root.mainloop()
            root.destroy()
            pass
    else:
            print("INVALID PASSWORD")
            print('')
            print("please try again")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            #os.system('cls')
            #login()

    
login_window = tk.Tk()
login_window.title("Login")



tk.Label(login_window, text = "Welcome! Please Log in.").pack()

tk.Label(login_window, text = "Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text = "Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

button = tk.Button(login_window, text = "Log In", command=Login)
button.pack(padx=20, pady= 20)

login_window.mainloop()


        

#login()