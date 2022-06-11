import random
print("Welcome to Rock Paper Scissors Game!")
print("------------------")
#variables
cpuscore = 0
playerscore = 0
tiescore = 0
possibleoutcomes = ["P","R","S"]
def checkWinner(playerOutcome, computerOutcome):
  if(playerOutcome == "R" and computerOutcome == "P"):
      print("Sorry!! you lost")
      return"cpu"
  elif(playerOutcome == "R") and computerOutcome =="S":
      print("Hurray!! you won")
      return "player" 
  elif(playerOutcome== "S" and computerOutcome== "P"):
       print("Hurray!! you won")
       return "player"
        
  elif (playerOutcome== "S" and computerOutcome== "R"):
       print("Sorry!! you lost")
       return "cpu"  
  elif (playerOutcome== "P" and computerOutcome== "R"):
       print("Hurray!! you won")
       return "player"

  elif (playerOutcome== "P" and computerOutcome== "S"):
       print("Sorry!! you lost")
       return "cpu"

  else:
       print("Tie!! play again to break the tie")
       return "tie"   
while(playerscore != 3 and cpuscore != 3):
      #validation
  while True:
      playeroutcome = input("\nChoose a possible outcome. R, P, or S: ")
      if(playeroutcome == "R" or playeroutcome == "S" or playeroutcome == "P"):
         break
      else:
       print("incorrect input. Retry")
  computerOutcome = (random.choice(possibleoutcomes))
  print("your outcome: ", playeroutcome)
  print("cpu outcome: ", computerOutcome)
  result = checkWinner(playeroutcome, computerOutcome)
  if(result == "player"):
       playerscore += 1
  elif(result == "cpu"):
       cpuscore += 1
  else:
       tiescore += 1 
  print("your sscore: ", playerscore, "CPU: ",cpuscore, " Ties: ", tiescore)


print ("Game over. Thank you for playing")