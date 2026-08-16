import random
n=random.randint(1,100)
a=-1
guesses=0
while (a!=n): 
    guesses+=1
    a=int(input("Guess a number:"))
    if(a>n):
        print("Lower number please")
    else:
        print("Higher number please")
print(f"you guessed the number {n} in guesses {guesses} correctly")