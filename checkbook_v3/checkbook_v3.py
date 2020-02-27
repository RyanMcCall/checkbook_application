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

def say_positive_exit():
    '''Accepts no arguments and prints message'''
    print()
    print("Sorry, input must be a positive number.")
    print("-- If you would like to return to menu, enter menu.")
    print()

def show_menu():
    '''Accepts no arguments and prints menu'''
    print()
    print("How can I help you?")
    print()
    print("1) View Current Balance")
    print("2) Record a Debit (withdraw)")
    print("3) Record a Credit (deposit)")
    print("4) Show all transaction history")
    print("5) Exit")
    print()

def exit_taco():
    '''Accepts no arguments and prints exit message'''
    print()
    print("🌮🌮🌮 Thank you for using T.A.C.O.! 🌮🌮🌮")
    print()

def say_no_overdraft():
    '''Accpets no arguments and prints that account can't be overdrafted'''
    print()
    print("🌮 Sorry, current balance is ${:,.2f} and ${:,.2f} will overdraft the account.".format(current_balance(), debit_amount))
    print("-- If you would like to return to menu, enter menu.")
    print()

def show_current_balance():
    '''Accepts no arguments and prints current balance'''
    print()
    print("🌮 Current balance is: ${:,.2f}".format(current_balance()))

def say_invalid_user_choice():
    '''Accepts no arguments and prints that choice is invalid'''
    print()
    print("🌮 Sorry, your choice must be 1, 2, 3, 4, or 5.")
    print()

def say_debiting(amount):
    '''Accepts amount and prints that the amount is debited'''
    print()
    print("🌮 Debiting ${:,.2f} from your balance.".format(amount))

def say_crediting(amount):
    '''Accepts amount and prints that the amount is credited'''
    print()
    print("🌮 Crediting ${:,.2f} to your balance.".format(amount))

def show_transaction_history():
    transactions = get_transaction_history()

    print()
    print("🌮🌮🌮 Transaction History 🌮🌮🌮")

    for transaction in transactions:
        if transaction > 0:
            print("Credit: ${:,.2f}".format(transaction))
        elif transaction < 0:
            transaction = transaction * -1
            print("Debit: -${:,.2f}".format(transaction))

# Checks if transaction_history.txt exist and if it doesn't, creates it with nothing in it.    
if not path.isfile("transaction_history.txt"):
    with open("transaction_history.txt", "a") as f:
        pass

print()
print("🌮🌮🌮 Welcome to the Terminal Assisted Checkbook Organizer! 🌮🌮🌮")

# Runs until 4 is selected
while True:
    show_menu()
    
    # This loop runs until the user provides a valid menu choice
    while True:
        user_choice = input("Your Choice? ")

        if not user_choice.isdigit():
            say_invalid_user_choice()
            continue

        user_choice = int(user_choice)

        if user_choice > 5 or user_choice < 1:
            say_invalid_user_choice()
            continue
        else:
            break

    if user_choice == 1:
        show_current_balance()
        
    #If user chooses 2, withdraw money
    elif user_choice == 2:
        print()
        # This loop runs until the user provides a valid deposit amount
        # (must be float or int and not higher than current balance)
        while True:
            debit_amount = input("How much would you like to debit? $")
            debit_amount = handle_commas(debit_amount)
            
            # Verify that the user has provided a float, int, or exit request
            if isfloat(debit_amount):
                if float(debit_amount) <= 0:
                    say_positive_exit()
                    continue
                debit_amount = round(float(debit_amount), 2)
            elif debit_amount.isdigit():
                if int(debit_amount) <= 0:
                    say_positive_exit()
                    continue
                debit_amount = float(debit_amount)
            elif debit_amount.lower() == "menu":
                break
            else:
                say_positive_exit()
                continue

            # Verify that the debit amount won't overdraw the account
            if debit_amount > current_balance():
                say_no_overdraft()
                continue
            else:
                say_debiting(debit_amount)
                # Store the debit as a negative for use in summation
                debit_amount = debit_amount * -1
                break

        # If user typed exit then this won't run, else it stores the transaction
        if type(debit_amount) == float:    
            with open("transaction_history.txt", "a") as f:
                f.write(str(debit_amount) + "\n")

    elif user_choice == 3:
        print()

        while True:
            credit_amount = input("How much would you like to credit? $")
            credit_amount = handle_commas(credit_amount)

            # Verify that the user has provided a float, int, or exit request
            if isfloat(credit_amount):
                if float(credit_amount) < 0:
                    say_positive_exit()
                    continue
                credit_amount = round(float(credit_amount), 2)
                say_crediting(credit_amount)
                break
            elif credit_amount.isdigit():
                if int(credit_amount) < 0:
                    say_positive_exit()
                credit_amount = float(credit_amount)
                say_crediting(credit_amount)
                break
            elif credit_amount.lower() == "menu":
                break
            else:
                say_positive_exit()
                continue

        # If user typed exit then this won't run, else it stores the transaction 
        if type(credit_amount) == float:
            with open("transaction_history.txt", "a") as f:
                f.write(str(credit_amount) + "\n")

    elif user_choice == 4:
        show_transaction_history()

    # If user chooses 5, exit the program
    elif user_choice == 5:
        exit_taco()
        break