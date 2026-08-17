from random import randint
'''
1 for rock
-1 for paper
0 for scissor
'''
computer=randint(-1,1)
you=input("Enter you choice:")
youDict={"r":1,"p":-1,"s":0}
youNum=youDict[you]

if(computer==youNum):
    print("It's a draw")

elif(computer==-1 and youNum==1):
    print("You win!")
    
elif(computer==-1 and youNum==0):
    print("You Lose!")
    
elif(computer==1 and youNum==-1):
    print("You Lose!")
    
elif(computer==1 and youNum==0):
    print("You win!")
    
elif(computer==0 and youNum==-1):
    print("You Win!")
    
elif(computer==0 and youNum==1):
    print("You Lose!")

else:
    print("Something went wrong!")
 