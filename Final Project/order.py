import os

# 📌 CONSTANTS  TODO We will replace by reading into from a text file
# A constant is a value we do not plan to change while the program runs.
# We use ALL CAPS for constants so they are easy to spot.
# 📌 CONSTANTS: these are our "menu options" (fixed choices) for the user to pick from.
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


def clear_screen():

    _ = os.system("cls" if os.name == "nt" else "clear")


def get_order(emp_id):
    # 🧠 STEP 2: Collect a drink order
    # Inputs:
    # - emp_id: the employee's ID number (so we can connect the order to a person)
    # ✅ Return: an order (right now we store it as a list)
    # 🧠 STEP 2: Get an order for this employee
    # Plan:
    # 1) Check if this employee has prior orders saved.
    # 2) If yes, list the 5 most recent orders (number them 1–5).
    # 3) Ask if they want to repeat an order number.
    # 4) If not repeating, display the menu and collect new choices (milk, roast, size, etc.).
    #
    clear_screen()
    while True:
        # 🖨️ Display the menu with numbers starting at 1 (friendlier for humans)
        count = 1
        for drink in DRINK_TYPE:
            print(f"{count}.   {drink}")
            count += 1
        try:
            # ⚠️ pitfall: `type` is also the name of a built-in Python function.
            # Using it as a variable works, but can be confusing. (A clearer name: drink_choice)
            type = int(
                input(
                    "Please enter the number for the type of drink you want:  "
                ).strip()
            )
        except ValueError:
            # 🛡️ Error handling: if they type letters instead of a number, int(...) fails.
            # ⚠️ Common bug: use len(DRINK_TYPE), not DRINK_TYPE.len()
            input(
                f"Please enter a number (1-{len(DRINK_TYPE)}). Press Enter to continue..."
            )
            continue
        if type < 1 or type > len(DRINK_TYPE):
            input(
                f"Please enter a number (1-{len(DRINK_TYPE)}). Press Enter to continue..."
            )
            continue
        # ℹ️ info: We subtract 1 because users choose 1..N, but Python indexes are 0..N-1.
        drink = DRINK_TYPE[type - 1]
        break

    clear_screen()
    while True:
        # 🖨️ Display the size menu
        count = 1
        for size in SIZES:
            print(f"{count}.   {size}")
            count += 1
        try:
            my_size = int(
                input(
                    "Please enter the number for the size of drink you want:  "
                ).strip()
            )
        except ValueError:
            # ⚠️ Common bug: use len(SIZES), not SIZES.len()
            input(f"Please enter a number (1-{len(SIZES)}). Press Enter to continue...")
            continue
        if my_size < 1 or my_size > len(SIZES):
            input(f"Please enter a number (1-{len(SIZES)}). Press Enter to continue...")
            continue
        size = SIZES[my_size - 1]
        break

    clear_screen()
    while True:
        # 🖨️ Display the milk menu
        count = 1
        for milk in MILKS:
            print(f"{count}.   {milk}")
            count += 1
        try:
            my_milk = int(
                input("Please enter the number for the milk you want:  ").strip()
            )
        except ValueError:
            # ⚠️ Common bug: use len(MILKS), not MILKS.len()
            input(f"Please enter a number (1-{len(MILKS)}). Press Enter to continue...")
            continue
        if my_milk < 1 or my_milk > len(MILKS):
            input(f"Please enter a number (1-{len(MILKS)}). Press Enter to continue...")
            continue
        milk = MILKS[my_milk - 1]
        break

    clear_screen()
    while True:
        # 🖨️ Display the flavor menu
        count = 1
        for flavor in FLAVORS:
            print(f"{count}.   {flavor}")
            count += 1
        try:
            my_flavor = int(
                input("Please enter the number for the flavor you want:  ").strip()
            )
        except ValueError:
            # ⚠️ Common bug: use len(FLAVORS), not FLAVORS.len()
            input(
                f"Please enter a number (1-{len(FLAVORS)}). Press Enter to continue..."
            )
            continue
        if my_flavor < 1 or my_flavor > len(FLAVORS):
            input(
                f"Please enter a number (1-{len(FLAVORS)}). Press Enter to continue..."
            )
            continue
        flavor = FLAVORS[my_flavor - 1]
        break

    while True:
        try:
            # 🧠 Ask for the number of flavor pumps (extra flavor shots)
            pumps = int(
                input(
                    "Please enter the number of pumps you want (ten cents each):  "
                ).strip()
            )
            if pumps < 0:
                print("Pumps cannot be negative. ")
                continue
            if pumps > 10:
                print("Ten is the maximum number of pumps. ")
                continue
        except ValueError:
            # 🛡️ If they type something that is not a number, don't crash—ask again.
            input(f"Please enter a number (0-10). Press Enter to continue...")
            continue
        break

    # ℹ️ info: This order is stored as a list. Each position has a meaning:
    # order[0]=emp_id, order[1]=drink, order[2]=size, order[3]=milk, order[4]=flavor, order[5]=pumps
    order = [emp_id, drink, size, milk, flavor, pumps]

    return order


def confirm_order(order):
    # 🧠 STEP 3: Confirm an order (show it back to the user and allow edits)
    # ✅ Return: the updated order list
    while True:
        clear_screen()
        count = 1
        # 🖨️ Display the order with numbers starting at 1 (easier for people to choose a line to edit)
        for item in order:
            print(f"{count}.  {item}")
            count += 1
        try:
            correct = input("Is everything correct (Y/N)").strip().upper()
            if correct == "Y":
                return order
            if correct != "N":
                input("Please enter Y or N. Press Enter to continue...")
                continue

            change = int(input("Please enter the number you want to change:  ").strip())
        except ValueError:
            # ⚠️ Common bug: lists don't have .length(); the Python way is len(order)
            input(f"Please enter a number (1-{len(order)}). Press Enter to continue...")
            continue

        try:
            if change < 1 or change > len(order):
                input(
                    f"Please enter a number (1-{len(order)}). Press Enter to continue..."
                )
                continue
            # ℹ️ info: change is 1-based for the user, so we use change-1 for the list index.
            new_value = input(f"Please enter the new value for {order[change-1]}")
            order[change - 1] = new_value
            # 💡 tip: We use `continue` (loop again) instead of calling confirm_order(order) again.
            # That keeps the logic in one loop and avoids recursion.
            continue
        except Exception as e:
            print(f"{e}\nThat was not a valid entry. Try again")
            input("Press Enter to continue...")
            continue
