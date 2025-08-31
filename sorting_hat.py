Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1) Do you like Dawn or Dusk ? \n 1) Dawn \n 2) Dusk")
q1 = int(input("1 for dawn , 2 for dusk\n"))

if q1 == 1 :
  Gryffindor += 1
  Ravenclaw  += 1
elif q1 == 2 :
  Hufflepuff += 1
  Slytherin  += 1
else :
  print("Wrong Input")

print("Q2) When I'm dead , I want people to remember me as: \n1) The Good \n2) The Great\n3) The Wise\n4) The Bold")
q2 = int(input("1 for the good , 2 for the great , 3 for the wise , 4 for the bold\n"))

if q2 == 1:
  Hufflepuff += 2
elif q2 == 2:
  Slytherin +=2 
elif q2 == 3:
  Ravenclaw += 2
elif q2 ==4:
  Gryffindor += 2
else:
  print("wrong input")

print("Q3) Which kind of instrument most pleases your ear?\n1) The violen\n2) The trumpet\n3) The piano\n4) The drum\n")
q3 = int(input("1 for the violin , 2 for the trumpet , 3 for the piano , 4 for the drum\n"))

if q3 == 1:
  Slytherin += 4
elif q3 == 2:
  Hufflepuff +=4
elif q3 == 3:
  Ravenclaw += 4
elif q3 == 4:
  Gryffindor += 4
else:
  print("wrong answer")

print("Your Scores in : Slytherin =" , Slytherin)  
print("Your Scores in : Hufflepuff =" , Hufflepuff)
print("Your Scores in : Ravenclaw =" , Ravenclaw)
print("Your Scores in : Gryffindor =" , Gryffindor)