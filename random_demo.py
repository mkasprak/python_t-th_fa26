"""
random and string verification
"""

# import
import random

while True:
    # continue till user says to stop
    number = random.randint(0, 100)
    print(number)
    try:
        guess = int(input("Again? (y/n)").lower().strip())
        if guess == number:
            print("You win!")
            break
        else:
            distance = abs(number - guess)
            if distance < 10:
                print("Hot")
            elif distance < 20:
                print("Warm")
            else:
                print("Cold")
    except Exception as e:
        print(e)
