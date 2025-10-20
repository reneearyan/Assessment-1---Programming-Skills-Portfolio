"""
Simple Search
"""
print("Simple Search")
name= ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name=input("Enter the name you want to search: ") #asks the user to input the name they're searching for

if search_name.lower() in [name.lower() for name in name]: #converts both the user input and the list items to lowercase and makes it case insensitive
    print(f"{search_name} was found in the list!") #prints if the user's the input is in the list
else:
    print(f"{search_name} was not found in the list.")#prints if the user's input is not in the list
