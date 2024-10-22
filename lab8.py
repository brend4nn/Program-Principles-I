correct_password = "1234"
try_again = "y"

while try_again == "y":
    password = input("Enter the password:")
    
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password.")
        try_again = input("Do you want to try again? (y/n)")
        
    if try_again == "n":
        print("Goodbye!")
