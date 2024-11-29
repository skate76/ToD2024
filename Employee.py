import datetime
import tkinter as tk
from tkinter import messagebox
from Order import OrderApp
from tkinter.scrolledtext import ScrolledText  # Import ScrolledText widget

class Employee:
    employee_list = []

    def __init__(self, employee_id, employee_name, employee_position, employee_username, employee_password, employee_phonenumber, employee_email, employee_payrate, status="Active", hours_worked=0):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.position = employee_position
        self.username = employee_username
        self.password = employee_password
        self.phonenumber = employee_phonenumber
        self.email = employee_email
        self.attendance_r = []  # Stores attendance records (check-in/check-out times)
        self.payrate = employee_payrate
        self.status = status
        self.hours_worked = hours_worked  # Store the hours worked
        Employee.employee_list.append(self)

    @classmethod
    def add_employee(cls, employee_id, employee_name, employee_position, employee_username, employee_password, employee_phonenumber, employee_email, employee_payrate, status="Active"):
        new_employee = Employee(employee_id, employee_name, employee_position, employee_username, employee_password, employee_phonenumber, employee_email, employee_payrate, status)
        cls.save_employees()  # Save to file after adding employee (new feature)
        return f"Employee {employee_name} added successfully!"

    @classmethod
    def display_employees(cls):
        if cls.employee_list:
            employee_info = ""
            for e in cls.employee_list:
                employee_info += (
                    f"ID: {e.employee_id}\n"
                    f"Name: {e.employee_name}\n"
                    f"Position: {e.position}\n"
                    f"Phone: {e.phonenumber}\n"
                    f"Email: {e.email}\n"
                    f"Pay Rate: {e.payrate}\n"
                    f"Status: {e.status}\n"
                    f"Hours Worked: {e.hours_worked}\n\n"  # Display hours worked
                )
            return employee_info
        else:
            return "No employees found."

    @classmethod
    def check_in(cls, employee_id, check_in_time):
        employee = cls.employee_finder(employee_id)
        if employee:
            employee.attendance_r.append([check_in_time, None])  # Append check-in time, check-out will be None
            cls.save_employees()  # Save updated attendance (new feature)
            return f"{employee.employee_name} checked in at {check_in_time}."
        return "Employee not found."

    @classmethod
    def check_out(cls, employee_id, check_out_time):
        employee = cls.employee_finder(employee_id)
        if employee:
            for record in employee.attendance_r:
                if record[1] is None:  # If check-out hasn't been recorded
                    record[1] = check_out_time
                    # Calculate the hours worked
                    check_in_time = datetime.datetime.strptime(record[0], "%I:%M %p")
                    check_out_time = datetime.datetime.strptime(check_out_time, "%I:%M %p")
                    hours_worked = (check_out_time - check_in_time).seconds / 3600  # Convert seconds to hours
                    employee.hours_worked += hours_worked
                    cls.save_employees()  # Save updated attendance and hours worked
                    return f"{employee.employee_name} checked out at {check_out_time.strftime('%I:%M %p')}. Hours worked: {hours_worked}."
            return f"{employee.employee_name} hasn't checked in yet."
        return "Employee not found."

    @classmethod
    def update_employee_contact(cls, employee_id, new_phone=None, new_email=None, new_position=None, new_payrate=None, new_status=None):
        employee = cls.employee_finder(employee_id)
        if employee:
            # Update the fields only if new values are provided
            if new_phone:
                employee.phonenumber = new_phone
            if new_email:
                employee.email = new_email
            if new_position:
                employee.position = new_position
            if new_payrate:
                employee.payrate = new_payrate
            if new_status:
                employee.status = new_status
            cls.save_employees()  # Save updated contact details (new feature)
            return f"Details for {employee.employee_name} updated successfully!"
        return "Employee not found."

    @classmethod
    def attendance_viewer(cls, employee_id):
        employee = cls.employee_finder(employee_id)
        if employee:
            records = ""
            if employee.attendance_r:
                for idx, record in enumerate(employee.attendance_r, 1):
                    check_in, check_out = record
                    records += f"Day {idx}: Checked in at {check_in} | Checked out at {check_out if check_out else 'Not checked out yet'}\n"
            else:
                records = "No attendance records found."
            return records
        return "Employee not found."

    @classmethod
    def employee_finder(cls, employee_id):
        for employee in cls.employee_list:
            if employee.employee_id == employee_id:
                return employee
        return None

    @classmethod
    def load_employees(cls):
        try:
            with open("employee2.txt", "r") as file:
                for line in file:
                    details = line.strip().split(", ")

                    if len(details) >= 10:  # Ensure valid employee data with 10 fields (including hours worked)
                        employee_id = int(details[0].split(": ")[1])
                        employee_name = details[1].split(": ")[1]
                        employee_position = details[2].split(": ")[1]
                        employee_username = details[3].split(": ")[1]
                        employee_password = details[4].split(": ")[1]
                        employee_phonenumber = details[5].split(": ")[1]
                        employee_email = details[6].split(": ")[1]
                        employee_payrate = float(details[7].split(": ")[1])
                        employee_status = details[8].split(": ")[1]
                        hours_worked = float(details[9].split(": ")[1]) if len(details) == 10 else 0

                        # Creating Employee object
                        Employee(employee_id, employee_name, employee_position, employee_username, employee_password, employee_phonenumber, employee_email, employee_payrate, employee_status, hours_worked)
        except FileNotFoundError:
            print("No employee file found. Creating a new one.")
            cls.employee_initialization()

    @classmethod
    def save_employees(cls):
        with open("employee2.txt", "w") as file:
            for employee in cls.employee_list:
                file.write(f"ID: {employee.employee_id}, Name: {employee.employee_name}, Position: {employee.position}, Username: {employee.username}, Password: {employee.password}, Phone: {employee.phonenumber}, Email: {employee.email}, Pay Rate: {employee.payrate}, Status: {employee.status}, Hours Worked: {employee.hours_worked}\n")

    @classmethod
    def employee_initialization(cls):
        Employee(1, "Justin Moo", "Manager", "employee1", "password1", "123-456-7890", "justin@example.com", 20.00)
        Employee(2, "Katelyn Tait", "Cashier", "employee2", "password2", "123-456-7891", "katelyn@example.com", 20.00)
        Employee(3, "Nasya Burrell", "Cashier", "employee3", "password3", "123-456-7891", "nasya@example.com", 20.00)
        Employee(4, "Tishawn Whyte", "Cashier", "employee4", "password4", "123-456-7891", "tishawn@example.com", 20.00)
        Employee(5, "Johnathon Bennet", "Cashier", "employee5", "password5", "123-456-7892", "johnathon@example.com", 20.00)
        Employee(6, "Dominic Adams", "Cashier", "employee6", "password6", "123-456-7893", "dominic@example.com", 20.00)


# GUI Setup with Tkinter
class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

        # Adding the employee ID input field
        self.id_label = tk.Label(root, text="Employee ID:")
        self.id_label.pack(pady=5)
        self.id_entry = tk.Entry(root)
        self.id_entry.pack(pady=5)

        # Check-in and Check-out time input fields
        self.time_label = tk.Label(root, text="Enter time (e.g. 7:00 AM or 7:00 PM):")
        self.time_label.pack(pady=5)
        self.time_entry = tk.Entry(root)
        self.time_entry.pack(pady=5)

        # Buttons for actions
        self.check_in_button = tk.Button(root, text="Check In", command=self.check_in)
        self.check_in_button.pack(pady=10)

        self.check_out_button = tk.Button(root, text="Check Out", command=self.check_out)
        self.check_out_button.pack(pady=10)

        self.attendance_button = tk.Button(root, text="View Attendance", command=self.view_attendance)
        self.attendance_button.pack(pady=10)

        self.display_button = tk.Button(root, text="Display Employees", command=self.display_employees)
        self.display_button.pack(pady=10)

        # Add Employee button
        self.add_employee_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_employee_button.pack(pady=10)

        # Update Employee button
        self.update_employee_button = tk.Button(root, text="Update Employee", command=self.update_employee)
        self.update_employee_button.pack(pady=10)

        self.place_order_button = tk.Button(root, text="Place Customer Order", command=self.place_order)
        self.place_order_button.pack(pady=10)

    def check_in(self):
        employee_id = int(self.id_entry.get())
        check_in_time = self.time_entry.get()
        response = Employee.check_in(employee_id, check_in_time)
        messagebox.showinfo("Check In", response)

    def check_out(self):
        employee_id = int(self.id_entry.get())
        check_out_time = self.time_entry.get()
        response = Employee.check_out(employee_id, check_out_time)
        messagebox.showinfo("Check Out", response)

    def view_attendance(self):
        employee_id = int(self.id_entry.get())
        response = Employee.attendance_viewer(employee_id)
        messagebox.showinfo("Attendance", response)

    def display_employees(self):
        # Create a new window for displaying employees
        display_window = tk.Toplevel(self.root)
        display_window.title("Employee List")

        # Create a ScrolledText widget for displaying the employee list
        employee_info = Employee.display_employees()

        employee_display = ScrolledText(display_window, width=60, height=20)
        employee_display.pack(pady=10)

        employee_display.insert(tk.END, employee_info)
        employee_display.config(state=tk.DISABLED)  # Make it read-only

    def add_employee(self):
        # Open a new window to add employee details
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Employee")

        # Input fields for new employee details
        tk.Label(add_window, text="Employee ID:").pack(pady=5)
        id_entry = tk.Entry(add_window)
        id_entry.pack(pady=5)

        tk.Label(add_window, text="Name:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Position:").pack(pady=5)
        position_entry = tk.Entry(add_window)
        position_entry.pack(pady=5)

        tk.Label(add_window, text="Username:").pack(pady=5)
        username_entry = tk.Entry(add_window)
        username_entry.pack(pady=5)

        tk.Label(add_window, text="Password:").pack(pady=5)
        password_entry = tk.Entry(add_window)
        password_entry.pack(pady=5)

        tk.Label(add_window, text="Phone:").pack(pady=5)
        phone_entry = tk.Entry(add_window)
        phone_entry.pack(pady=5)

        tk.Label(add_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(add_window)
        email_entry.pack(pady=5)

        tk.Label(add_window, text="Pay Rate:").pack(pady=5)
        payrate_entry = tk.Entry(add_window)
        payrate_entry.pack(pady=5)

        def save_employee():
            employee_id = int(id_entry.get())
            name = name_entry.get()
            position = position_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            payrate = float(payrate_entry.get())

            response = Employee.add_employee(employee_id, name, position, username, password, phone, email, payrate)
            messagebox.showinfo("Add Employee", response)
            add_window.destroy()  # Close the add employee window

        # Add employee button
        tk.Button(add_window, text="Save Employee", command=save_employee).pack(pady=10)

    def update_employee(self):
        # Open a new window to update employee details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Employee")

        # Input field for employee ID
        tk.Label(update_window, text="Employee ID:").pack(pady=5)
        id_entry = tk.Entry(update_window)
        id_entry.pack(pady=5)

        # Input fields for new employee details
        tk.Label(update_window, text="New Phone (optional):").pack(pady=5)
        phone_entry = tk.Entry(update_window)
        phone_entry.pack(pady=5)

        tk.Label(update_window, text="New Email (optional):").pack(pady=5)
        email_entry = tk.Entry(update_window)
        email_entry.pack(pady=5)

        tk.Label(update_window, text="New Position (optional):").pack(pady=5)
        position_entry = tk.Entry(update_window)
        position_entry.pack(pady=5)

        tk.Label(update_window, text="New Pay Rate (optional):").pack(pady=5)
        payrate_entry = tk.Entry(update_window)
        payrate_entry.pack(pady=5)

        tk.Label(update_window, text="New Status (optional):").pack(pady=5)
        status_entry = tk.Entry(update_window)
        status_entry.pack(pady=5)

        def update_employee_details():
            employee_id = int(id_entry.get())
            phone = phone_entry.get() or None
            email = email_entry.get() or None
            position = position_entry.get() or None
            payrate = float(payrate_entry.get()) if payrate_entry.get() else None
            status = status_entry.get() or None

            response = Employee.update_employee_contact(employee_id, phone, email, position, payrate, status)
            messagebox.showinfo("Update Employee", response)
            update_window.destroy()  # Close the update window

        # Update employee button
        tk.Button(update_window, text="Update Employee", command=update_employee_details).pack(pady=10)
    
    def place_order(self):
        root= tk.Tk()
        OrderApp(root)

# Run the GUI
if __name__ == "__main__":
    Employee.load_employees()  # Load employees from the file at the start
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()