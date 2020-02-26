def handle_commas(string):
    ''' Accepts a string and returns a string with the commas removed '''
    return string.replace(",", "")

def isfloat(string):
    ''' Accepts a string and returns True if it contains only a float, else it returns False'''
    string = handle_commas(string)

    if string.isdigit():
        return False
    elif string.replace(".", "").isdigit():
        return True
    else:
        return False


print()
print("🌮🌮🌮 Welcome to the Terminal Assisted Checkbook Organizer! 🌮🌮🌮")
print()

run = True

while run:
    print("How can I help you?")
    print()
    print("1) View Current Balance")
    print("2) Record a Debit (withdraw)")
    print("3) Record a Credit (deposit)")
    print("4) Exit")
    print()
    
    # This loop runs until the user provides a valid menu choice
    while True:
        user_choice = input("Your Choice? ")

        if not user_choice.isdigit():
            print("Sorry, your choice must be 1, 2, 3, or 4.")
            print()
            continue

        user_choice = int(user_choice)

        if user_choice > 4 or user_choice < 1:
            print("Sorry, your choice must be 1, 2, 3, or 4")
            print()
            continue
        else:
            break

    # If user chooses 4, exit the program
    if user_choice == 4:
        print()
        print("🌮🌮🌮 Thank you for using T.A.C.O.! 🌮🌮🌮")
        print()
        run = False
        
    #If user chooses 2, withdraw money
    elif user_choice == 2:
        # This loop runs until the user provides a valid deposit amount
        while True:
            debit_amount = input("How much would you like to debit? $")

            if isfloat(debit_amount):
                break
            elif debit_amount.isdigit():
                break
            else:
                continue
        
        debit_amount = float(debit_amount)

        transaction_info = ["debit", debit_amount]

        with open("transaction_history.txt", "a") as f:
            f.writelines(str(transaction_info) + "\n")

        # Need to check if balance if balance goes below 0.