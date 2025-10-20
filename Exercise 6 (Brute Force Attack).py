"""
Brute Force Attack with Bonus
"""
correct_password="12345" #correct password
max_attempts= 5 #maximum attempts allowed
attempts_left= max_attempts #how many attempts are left

while attempts_left>0: #repeat while there are attempts left
    password=input("Enter the password: ") #asks the user to enter the password
    if password==correct_password: #checks if the password is correct
        print("Access granted. Welcome!")
        break; #if correct, it stops the loop
    attempts_left-=1 #subtract from remaining attempts
    if attempts_left>0: #gives feedback to the user
        print(f"You have {attempts_left} attempts left.")
    else:
        print("Wrong password. No attempts left.")