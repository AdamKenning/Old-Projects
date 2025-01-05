#get user choice
#get robot choice
#see who wins
#guess users next choice

import random

game = "ongoing"
rounds= 0
play=random.randint(1,3)
dwins=0
uwins=0
cwins=0

roundlist=[]
complist =[]
userlist =[]
winslist =[]

#for the game to continue multiple rounds
while game == "ongoing":
  rounds=rounds+1
  askchoice="yes"
  
  #displays round
  print("round: ",rounds)
  
  #get users choice
  while askchoice != "r" and askchoice != "p" and askchoice != "s" and askchoice != "q":
    askchoice=input("rock, paper or scissors (r,p,s) ('q' for results)")

  #convert user choice to either 1 , 2 , 3 for ease 
  if   askchoice=="r":
    userchoice="rock"
    userc=1
  elif askchoice=="p":
    userchoice="paper"
    userc=2
  elif askchoice=="s":
    userchoice="scissors"
    userc=3
  else:
    game="stop"
    
  #checkpoint incase user chose to quit
  if game =="ongoing":

    #computer decides if itll play randomly or according to users last turn
    decide=random.randint(1,4)
    #decide>0 = always choose based of logic
    #decide>2 = sometimes of logic, sometimes random
    #decide>4 = always choose randomly
    if decide>1:
      compc=play
    else:
      compc=random.randint(1,3)

    #converts computers choice to words   
    if   compc ==1:
      compchoice="rock"
      completter="r"
    elif compc ==2:
      compchoice="paper"
      completter="p"
    else:
      compchoice="scissors"
      completter="s"

    #decides who won
    if   compc==1:
      if   userc==1:
        winner="draw"
      elif userc==2:
        winner="user"
      else:
        winner="comp"
    elif compc==2:
      if   userc==1:
        winner="comp"
      elif userc==2:
        winner="draw"
      else:
        winner="user"
    else:
      if   userc==1:
        winner="user"
      elif userc==2:
        winner="comp"
      else:
        winner="draw"

    #logical guess on users next choice   
    if winner=="draw":
      winnerletter="d"
      dwins=dwins+1
      play=compc-1
      if play==0:
        play=3
    elif winner=="user":
      winnerletter="u"
      uwins=uwins+1
      play=userc+1
      if play==4:
        play=1
    else:
      winnerletter="c"
      cwins=cwins+1
      play=compc+1
      if play==4:
        play=1

    #displays outcome
    if   winner == "user":
      print("your win")
    elif winner == "draw":
      print("draw")
    else:
      print("your lose")
    print()
  
  else:
    pass

  #keeping track of stuff
  roundlist.append(str(rounds).rjust(2,' '))
  complist.append(completter)
  userlist.append(askchoice)
  winslist.append(winnerletter)
  
#displays extra info  
print()
print("wins :",uwins)
print("draws:",dwins)
print("loses:",cwins)
print()
print("rounds: ",*roundlist,sep='|')
print("comp  : ",*complist,sep='| ')
print("user  : ",*userlist,sep='| ')
print("winner: ",*winslist,sep='| ')

