print()
print("🌮🌮🌮 Welcome to the Terminal Assisted Checkbook Organizer! 🌮🌮🌮")
print()

open = True

while open:
    print("How can I help you?")
    print()
    print("1) View Current Balance")
    print("2) Record a Debit (withdraw)")
    print("3) Record a Credit (deposit)")
    print("4) Exit")
    print()
    
    

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


    if user_choice == 4:
        print()
        print("🌮🌮🌮 Thank you for using T.A.C.O.! 🌮🌮🌮")
        open = False