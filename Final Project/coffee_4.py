"""
☕ Final Project Menus

"""

import employee
import order
import datetime
import os

# 📌 Week 11 note (design decision):
# split into multiple files


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


# will read in
def print_label(order, employee):
    # 🧠 STEP 4: Output a label / receipt for the order
    # 🖨️ Output: this function is where you format what prints to the screen.
    # 🧠 STEP 4: Output (label / receipt)
    # Plan:
    # 1) Create the label text (employee + order details).
    # 2) Print the label to the screen (or to a printer later).
    # ℹ️ If `employee` is a dictionary, looping over it gives you the KEYS.
    # We use each key to print both the key and the value.
    for key in employee:
        print(f"{key}: {employee[key]}")
    for item in order:
        print(item)
    # 3) Ask if they also want a receipt.
    # 4) Print the receipt if requested.


def main():
    # ▶️ Entry point: main() runs the program "top to bottom" in order.
    # ▶️ main() is the "boss" function that runs the steps in order.
    # It collects results from one function and passes them into the next.
    clear_screen()
    # 🧠 Get the employee record first
    # emp_record is a dictionary
    emp_record = employee.get_employee()
    # ℹ️ Grab the employee number out of the dictionary using its key
    emp_id = emp_record["employee_nbr"]
    emp_record = employee.confirm_employee(emp_record)
    # ✅ We pass the employee ID (an int) into get_order so the order can be tied to a person.
    order = order.get_order(emp_id)
    order = order.confirm_order(order)


# ▶️ Start the program by calling main().
main()
