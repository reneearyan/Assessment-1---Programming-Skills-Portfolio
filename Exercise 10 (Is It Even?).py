"""
Is it even?
"""
def check_even_odd(number): #the function that determines if the value is even or odd 
    if number%2==0: #determines if the value is even or odd
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    number=int(input("Enter your number: ")) #asks the user for a number
    
    result=check_even_odd(number) 
    print(result) #prints the result
main() #calls the main function
    
    