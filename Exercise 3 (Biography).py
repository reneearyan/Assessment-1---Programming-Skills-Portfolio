"""
Biography with Bonus
"""
#user input
name = input("Enter your name: ") #user enters name
hometown = input("Enter your hometown: ") #user enters hometown

while True:
    age = input("Enter your age: ") #user enters age
    if age.isdigit():
        age=int(age)
        break;
    else: 
        print("\nPlease enter a valid number.")


person = {
    'Name': name, 
    'Hometown': hometown,
    'Age': age}

print(f"\nFull Biography\nName: {person['Name']}\nHometown: {person['Hometown']}\nAge: {person['Age']}")