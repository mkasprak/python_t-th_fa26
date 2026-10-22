"""
☕ Final Project Planning File (STUBS)

This file is intentionally *not finished yet*.
We are using stubs (`pass`) plus comments to plan the program first.

✅ Goal: write the plan in English, then turn each step into Python code later.

"""

# 📌 Week 10 note (design decision):
# We decided to pass around the employee's ID (employee_id), not the whole employee record.
# Next week, when we learn file I/O, we will use employee_id to look up the full employee info from the file.

# 📌 CONSTANTS
# A constant is a value we do not plan to change while the program runs.
# We use ALL CAPS for constants so they are easy to spot.
MILKS = ("Whole", "2%", "Skim", "Oat", "Soy", "Coconut", "None")
DRINK_TYPE = ("Americano", "Drip", "Latte", "Caffe au Lait", "Matcha", "Tea")
SIZES = ("Large", "Medium", "Small")
FLAVORS = (
    "Caramel",
    "Vanilla",
    "Chocolate",
    "Seasonal",
    "Sugar Free Caramel",
    "Sugar Free Vanilla",
    "None",
)

# ℹ️ info: Tuples are a fixed menu of choices (we do not add/remove options while running).


import os


def clear_screen():
    # Assigning to _ silences the system return code (0) in interactive shells
    # this code I looked up on the internet and was answered by AI (gemini)
    _ = os.system("cls" if os.name == "nt" else "clear")


def get_employee():
    # 🧠 STEP 1: Identify the employee
    # Plan:
    # 1) Ask for the employee number.
    # 2) Look up that employee in storage (ex: a text file).
    # 3) If the employee does not exist, collect info and create a new record.
    #
    # 📁 Data idea (text file):
    # EmployeeNumber, Name, OfficeNumber, Extension
    id = int(input("Please enter your ID number:  "))
    # TODO lookup employee
    f_name = input("Please enter your first name:  ")
    l_name = input("Please enter your last name:  ")
    office_nbr = input("Office to deliver to:  ")
    extension = input("Please enter extension:  ")
    known_allergies = input(
        "Please enter any known food allergies or sensitivities separated by commas:  "
    )
    #
    # ✅ Return value:
    # Return employee_id (ex: an int or string). We will use that ID to look up the full employee
    # information from the file when we need it (Week 10 file reading/writing).
    employee_record = {
        "employee_nbr": id,
        "office": office_nbr,
        "extension": extension,
        "f_name": f_name,
        "l_name": l_name,
        "allergies": known_allergies,
    }

    return employee_record


def get_order(employee_id):
    # 🧠 STEP 2: Get an order for this employee
    # Plan:
    # 1) Check if this employee has prior orders saved.
    # 2) If yes, list the 5 most recent orders (number them 1–5).
    # 3) Ask if they want to repeat an order number.
    # 4) If not repeating, display the menu and collect new choices (milk, roast, size, etc.).
    #
    clear_screen()
    while True:
        count = 1
        for drink in DRINK_TYPE:
            print(f"{count}.   {drink}")
            count += 1
        try:
            type = int(
                input("Please enter the number for the type of drink you want:  ")
            ).strip()
        except ValueError:
            input(
                f"Please enter a number (1-{DRINK_TYPE.len()}). Press Enter to continue..."
            )
            continue
        break

    clear_screen()
    while True:
        count = 1
        for size in SIZES:
            print(f"{count}.   {size}")
            count += 1
        try:
            size = int(
                input("Please enter the number for the size of drink you want:  ")
            ).strip()
        except ValueError:
            input(
                f"Please enter a number (1-{SIZES.len()}). Press Enter to continue..."
            )
            continue
        size = SIZES[count - 1]
        break

    clear_screen()
    while True:
        count = 1
        for milk in MILKS:
            print(f"{count}.   {milk}")
            count += 1
        try:
            milk = int(
                input("Please enter the number for the milk you want:  ")
            ).strip()
        except ValueError:
            input(
                f"Please enter a number (1-{MILKS.len()}). Press Enter to continue..."
            )
            continue
        milk = MILKS[count - 1]
        break

    clear_screen()
    while True:
        count = 1
        for flavor in FLAVORS:
            print(f"{count}.   {flavor}")
            count += 1
        try:
            flavor = int(
                input("Please enter the number for the flavor you want:  ")
            ).strip()
        except ValueError:
            input(
                f"Please enter a number (1-{FLAVORS.len()}). Press Enter to continue..."
            )
            continue
        flavor = FLAVORS[count - 1]
        break

    while True:
        try:
            pumps = int(
                input("Please enter the number of pumps you want (ten cents each):  ")
            ).strip()
            if pumps > 10:
                print("Ten is the maximum number of pumps. ")
                continue
        except ValueError:
            input(f"Please enter a number (0-10). Press Enter to continue...")
            continue
        break

    order = [drink, size, milk, flavor, pumps]


def confirm_employee(employee_record):
    while True:
        clear_screen()
        # confirm employee record
        print(f"1.  Employee Number:  {employee_record["employee_nbr"]}")
        print(f"2.  Office Number:  {employee_record["office"]}")
        print(f"3.  Extension:  {employee_record["extension"]}")
        print(f"4.  First Name:  {employee_record["f_name"]}")
        print(f"5.  Last Name:  {employee_record["l_name"]}")
        print(f"6.  Allergies: {employee_record["allergies"]}")
        # 3) Ask: "Is this correct? (y/n)"
        correct = input("Is this correct? (Y/N) ").strip().upper()
        if correct == "Y":
            break
        if correct != "N":
            input("Please enter Y or N. Press Enter to continue...")
            continue

        try:
            change = int(input("What number would you like to change? ").strip())
        except ValueError:
            input("Please enter a number (1-6). Press Enter to continue...")
            continue

        match change:
            case 1:
                while True:
                    try:
                        employee_nbr = int(input("New employee number: ").strip())
                        break
                    except ValueError:
                        print("Employee number must be a whole number.")
            case 2:
                office = input("New office number: ").strip()
            case 3:
                extension = input("New extension: ").strip()
            case 4:
                f_name = input("New first name: ").strip()
            case 5:
                l_name = input("New last name: ").strip()
            case 6:
                allergies = input("New allergies: ").strip()
            case _:
                input("Please choose a number 1-6. Press Enter to continue...")

    # 4) If YES → go to print_label(order, employee).
    # 5) If NO → allow changes, then save any updates.
    #
    # 💾 Saving:
    # If anything changes, update the employee and/or order storage so it is available next time.
    return employee_nbr, office, extension, f_name, l_name, allergies


def print_label(order, employee):
    # 🧠 STEP 4: Output (label / receipt)
    # Plan:
    # 1) Create the label text (employee + order details).
    # 2) Print the label to the screen (or to a printer later).
    # 3) Ask if they also want a receipt.
    # 4) Print the receipt if requested.
    pass


def main():
    # ▶️ main() is the "boss" function that runs the steps in order.
    # It collects results from one function and passes them into the next.
    clear_screen()
    # emp_record is a dictionary
    emp_record = get_employee()
    emp_id = emp_record["employee_nbr"]
    order = get_order(emp_id)
    emp_record = confirm_employee(emp_record)


# ▶️ Start the program by calling main().
main()
