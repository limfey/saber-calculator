print("Welcome, friend! This is a simple calculator made for Saber Interactive")


def calculator():
    while True:
        try:
            user_input = input("What would you like to solve?:\n")
            print(eval(user_input))
            ask_again = input("Would you like to try once more? Please type 'Yes' or 'No'\n")
            if ask_again == "No":
                break
            elif ask_again == "Yes":
                continue
            else:
                print("Sorry, math is serious, no jokes here!\n")
                break
        except (ZeroDivisionError, SyntaxError, NameError):
            print("Nope! You can't do it, sorry!\n")


calculator()
print("Have a nice day!")
