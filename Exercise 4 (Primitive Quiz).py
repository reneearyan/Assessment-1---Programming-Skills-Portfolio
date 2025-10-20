"""
Primitive Quiz with Bonus

"""

print("The Capitals of 10 European Countries Quiz")#prints the title of quiz

score = 0 #counts all correct answers

#Question 1
print("1. What is the capital of France?")
answer=input("Enter your answer: ")
if answer.lower()=="paris":
    print("The answer is correct.")
    score +=1 #adds up to score = 0
else:
    print("The answer is wrong.")
   
#Question 2 
print("2. What is the capital of Germany?")
answer=input("Enter your answer: ")
if answer.lower()=="berlin":
    print("The answer is correct.")
    score +=1 #adds up to score = 0
else:
    print("The answer is wrong.")

#Question 3
print("3. What is the capital of Italy?")
answer=input("Enter your answer: ")
if answer.lower()=="rome":
    print("The answer is correct.")
    score +=1 #adds up to score = 0
else:
    print("The answer is wrong.")
    
#Question 4
print("4. What is the capital of Spain?")
answer=input("Enter your answer: ")
if answer.lower()=="madrid":
    print("The answer is correct.")
    score +=1  #adds up to score = 0
else:
    print("The answer is wrong.")
    
#Question 5 
print("5. What is the capital of Portugal?")
answer=input("Enter your answer: ")
if answer.lower()=="lisbon":
    print("The answer is correct.")
    score +=1  #adds up to score = 0
else:
    print("The answer is wrong.")

#Question 6
print("6. What is the capital of Netherlands?")
answer=input("Enter your answer: ")
if answer.lower()=="amsterdam":
    print("The answer is correct.")
    score +=1  #adds up to score = 0
else:
    print("The answer is wrong.")
   
#Question 7
print("7. What is the capital of Belgium?")
answer=input("Enter your answer: ")
if answer.lower()=="brussels":
    print("The answer is correct.")
    score +=1 #adds up to score = 0
else:
    print("The answer is wrong.")

#Question 8
print("8. What is the capital of Switzerland?")
answer=input("Enter your answer: ")
if answer.lower()=="bern":
    print("The answer is correct.")
    score +=1 #adds up to score = 0
else:
    print("The answer is wrong.")
    
#Question 9
print("9. What is the capital of Austria?")
answer=input("Enter your answer: ")
if answer.lower()=="vienna":
    print("The answer is correct.")
    score +=1 #adds up to score = 0
else:
    print("The answer is wrong.")
    
#Question 10 
print("10. What is the capital of Poland?")
answer=input("Enter your answer: ")
if answer.lower()=="warsaw":
    print("The answer is correct.")
    score +=1 #adds up to score = 0
else:
    print("The answer is wrong.")
    
#Prints the total score
print(f"\nScore: {score}/10")

