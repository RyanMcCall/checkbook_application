print()
print("~~~ Welcome to the Terminal Checkbook App! ~~~")
print()

dont_exit = True

while dont_exit:
    print("How can I help you?")
    print()
    print("1) View Current Balance")
    print("2) Record a Debit (withdraw)")
    print("3) Record a Credit (deposit)")
    print("4) Exit")
    print()
    
    user_choice = input("Your Choice? ")

    if user_choice == "4":
        dont_exit = False
