import random
def play():
 while"true":
  user=int(input("enter your choice( type 0 for rock,1 for paper,2 for scissor):"))
  computer=random.randint(0,2)
  print(f"user:{user}")
  print(f"computer:{computer}")
  if(computer==user):
    print("its tie")
  elif(computer==0 and user==2):
    print("you lose")
  elif(computer==1 and user==2):
     print("you win")
  elif(computer==2 and user==2):
    print("its tie")
  elif(user==0 and computer==1):
    print("you lose")
  elif(user==0 and computer==2):
    print("you win")
  elif(user==0 and computer==0):
    print("its tie")
  elif(user==1 and computer==0):
    print("you won")
  elif(user==1 and computer==2):
    print("you lose")
  else:
    print("invalid statement")
  play_again=input("do you want play again(yes or no):").lower()
  if play_again=="no":
     print("thanks for playing")
     break
  
play()



    

