import random
import time
l = ["rock","scissor","paper"]



while True :
 Ccount= 0
 Ucount=0
 uc =int(input('''
Game start......
1 YES
2 NO | EXIT  
'''))
 if uc==1 :
  pass
  for i in range(1,6):
   U= int(input('''
1  Rock
2 Scissor
3 Paper
   '''))
   if U==1 :
    uchoice= "rock"
   elif U==2 :
    uchoice= "scissor"
   elif U==3 :
    uchoice= "paper"
   Cchoice=random.choice(l)
   if uchoice==Cchoice :
    print("you enter",uchoice)
    print("computer enter",Cchoice)
    print("Game Draw")
    
    
   elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper") :
    print("you enter",uchoice)
    print("computer enter",Cchoice)
    print("you win")
    Ucount=Ucount+1
   else :
    print("you enter",uchoice)
    print("computer enter",Cchoice)
    print("computer win")
    Ccount=Ccount+1
  if Ucount==Ccount :
    print("Final Game Draw...")
    print("your score :",Ucount)
    print("computer score :",Ccount)
    
     
     
  elif Ucount > Ccount :
    print("Final  you win the game...")
    print("your score :",Ucount)
    print("computer score :",Ccount)
  else :
    print("Final  computer win the game...")
    print("your score :",Ucount)
    print("computer score :",Ccount)
    
   
  
  
  
  
  
  
 else :
  time.sleep(1)
  print("Thanks for using this game")
  break