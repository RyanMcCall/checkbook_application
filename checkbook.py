from os import path

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

def clean_strings(string):
    '''Accepts a string and returns it without newline characters'''
    return string.replace("\n", "")

def get_transaction_history():
    '''Accepts no arguments and return a list of floats from transaction_history.txt'''
    with open("transaction_history.txt") as f:
        transactions = f.readlines()
    
    clean_transactions = [float(clean_strings(transaction)) for transaction in transactions]

    return clean_transactions

def current_balance():
    '''Accepts no arguments and return a a sum of the transactions from get_transaction_history()'''
    current_account_balance = sum(get_transaction_history())
    return current_account_balance
    
if not path.isfile("transaction_history.txt"):
    with open("transaction_history.txt", "a") as f:
        pass

print()
print("🌮🌮🌮 Welcome to the Terminal Assisted Checkbook Organizer! 🌮🌮🌮")

run = True

# Runs until 4 is selected
while run:
    print()
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
        print()
        # This loop runs until the user provides a valid deposit amount
        # (must be float or int and not higher than current balance)
        while True:
            debit_amount = input("How much would you like to debit? $")
            
            # Verify that the user has provided a float or int
            if isfloat(debit_amount):
                if float(debit_amount) < 0:
                    print()
                    print("Sorry, debits must be positive numbers.")
                    print()
                    continue
                debit_amount = float(debit_amount)
            elif debit_amount.isdigit():
                if int(debit_amount) < 0:
                    print()
                    print("Sorry, debits must be positive numbers.")
                    print()
                    continue
                debit_amount = float(debit_amount)
            else:
                print("Sorry, debits must be a positive number.")
                continue

            # Verify that the debit amount won't overdraw the account
            if debit_amount > current_balance():
                print("Sorry, current balance is", current_balance(), "and", debit_amount, "will overdraft the account")
                continue
            else:
                debit_amount = debit_amount * -1
                break

        with open("transaction_history.txt", "a") as f:
            f.write(str(debit_amount) + "\n")

    elif user_choice == 1:
        print()
        print("Current balance is:", current_balance())
        print()

    elif user_choice == 3:
        print()

        while True:
            credit_amount = input("How much would you like to credit? $")

            if isfloat(credit_amount):
                if float(credit_amount) < 0:
                    print()
                    print("Sorry, debits must be positive numbers.")
                    print()
                    continue
                credit_amount = float(credit_amount)
                break
            elif credit_amount.isdigit():
                if int(credit_amount) < 0:
                    print()
                    print("Sorry, debits must be positive numbers.")
                    print()
                credit_amount = float(credit_amount)
                break
            else:
                print("Sorry, debits must be a positive number.")
                continue

        with open("transaction_history.txt", "a") as f:
            f.write(str(credit_amount) + "\n")