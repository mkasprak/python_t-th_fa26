"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# ℹ️ Madlibs program

# ℹ️ Get input, store in variables
print("\t\t\t\tMadlibs - Mary had a Little Lamb\n\n")
name = input("Enter a person's name: ")
animal = input("Enter a kind of animal: ")
color = input("Enter a color: ")


# ℹ️ Output

print(f"\n\n{name} had a little {animal}")
print(f"Whose fleece was {color} as snow")
print(f"And everywhere that {name} went")
print(f"The {animal} was sure to go")
