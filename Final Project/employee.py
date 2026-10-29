import os


def clear_screen():
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
    # ⚠️ pitfall: naming a variable `id` hides Python's built-in id() function.
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

    # ✅ Return: a dictionary (dict) so we can keep employee info with NAMEs (keys).
    # 💡 tip: you can access a value by key, like employee_record["office"].
    employee_record = {
        "employee_nbr": id,
        "office": office_nbr,
        "extension": extension,
        "f_name": f_name,
        "l_name": l_name,
        "allergies": known_allergies,
    }

    return employee_record


def confirm_employee(employee_record):
    # 🧠 STEP 1b: Confirm employee info (print the record, let the user fix mistakes)
    # ✅ Return: the (possibly updated) employee_record dictionary
    while True:
        clear_screen()
        # confirm employee record
        # NOTE: This is an f-string. The string itself uses double quotes: f"..."
        # Inside the { ... } part we also need quotes for dict keys. If we used double quotes
        # again (employee_record["office"]), Python would think the f-string ended early.
        # Using single quotes for the dict keys avoids that quote-conflict.
        print(f"1.  Employee Number:  {employee_record['employee_nbr']}")
        print(f"2.  Office Number:  {employee_record['office']}")
        print(f"3.  Extension:  {employee_record['extension']}")
        print(f"4.  First Name:  {employee_record['f_name']}")
        print(f"5.  Last Name:  {employee_record['l_name']}")
        print(f"6.  Allergies: {employee_record['allergies']}")
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

        # ⚠️ Important concept:
        # `employee_record` is the dictionary we want to update.
        # If you want the change to "stick", you must assign into the dict (example):
        # employee_record["office"] = input("New office number: ").strip()
        match change:
            case 1:
                while True:
                    try:
                        employee_nbr = int(input("New employee number: ").strip())
                        employee_record["employee_nbr"] = employee_nbr
                        break
                    except ValueError:
                        print("Employee number must be a whole number.")
            case 2:
                employee_record["office"] = input("New office number: ").strip()
            case 3:
                employee_record["extension"] = input("New extension: ").strip()
            case 4:
                employee_record["f_name"] = input("New first name: ").strip()
            case 5:
                employee_record["l_name"] = input("New last name: ").strip()
            case 6:
                employee_record["allergies"] = input("New allergies: ").strip()
            case _:
                input("Please choose a number 1-6. Press Enter to continue...")

    # 4) If YES → go to print_label(order, employee).
    # 5) If NO → allow changes, then save any updates.
    #
    # 💾 Saving:
    # If anything changes, update the employee and/or order storage so it is available next time.

    return employee_record
