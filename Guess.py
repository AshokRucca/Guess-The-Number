import random 
n=random.randrange(1,10)
guess=int(input("Enter any number"))
while n!=guess:
    if guess < n:
        print("too low")
        guess=int(input("Enter any number"))
        
    elif  guess > n:
        print("Too High")
        guess=int(input("Enter any number"))
    else:
        break
print("You guessed it right!!")
