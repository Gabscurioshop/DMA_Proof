# This program performs the Abbott Costello Math Trick
#with a working set picked by the user

#Division Proof
def division(plier, plicand, product):
  print("First, check with division! ")
  print("See that " + plier + " goes into " + product + ".")
 
  m = int(plicand) // 10#multiplicand's tens place
  n = int(plicand) % 10#multiplicand's ones place
  x = int(product) // 10#product's tens place
  y = int(product) % 10#product's one place
  print(plier + " into " + str(x) + "?")
  print(plier+ " doesn't go into " + str(x)+ ".")
  print("No matter how hard you try, you can't squeeze that big " + plier + " into that little " + str(x) + ".")
  print("We're gonna take that little " + str(x) + " and keep it in your pocket. \n")
  print(plier+ " into " + str(y) + "? " + str(m)+ ".")
  print("Let's put that " + str(m)  + " in the quotient.")
  print("Now we're gonna take " + str(m) + " times " + plier + " and place it under the " + str(y) + ".")
  r = y % int(plier) #remainder
  print(str(y) + " minus " + str(m *int(plier)) + "? " + str(r) + ".")
  print("Now take that " + str(x)+ " out of your pocket and place it in front of the new dividend's " + str(r) + ".\n")
  print(plier+ " into " +str(10*x + r)+ "? " + str(n) + ".")
  print("Let's put that " + str(n) + " in the quotient too." );
  print("So, "+ plier + " into " + product + " is " + plicand + ".\n")

#Multiplication proof
def multiplication(plier, plicand, product):
  m = int(plicand) // 10#multiplicand's tens place
  n = int(plicand) % 10#multiplicand's ones place
  print("Not convinced yet? Let's check with multiplication.")
  print(plicand + " times " + plier + ".")
  sum1 = int(plier) * n
  sum2 = int(plier) * m
  print(plier + " times " + str(n) + "? " + str(sum1) + ".")
  print(plier + " times " + str(m) + "? " + str(sum2) + ".")
  print(str(sum1) + " plus " + str(sum2) + "? " + product+ ".\n")

#Addition Proof
def addition(plier, plicand, product):
  print("Still not conviced? Let's prove it with addition.")
  print("Add " + plicand + " " +plier + " times")
  m = int(plicand) // 10#multiplicand's tens place
  n = int(plicand) % 10#multiplicand's ones place
  sum1 = int(plier) * n
  print("First, add the ones column.")
  for i in range(1,int(plier)+1):
    print(i*n)
  print("Now, add that value with the tens column.")
  for j in range(1,int(plier)+1):
    print(sum1 + j*m)

f = open("workingCombos.txt", "r")

print ("Launching Abbott and Castello Math Trick \n")
val = input("Pick a set from 1 to 22. \n")
#Let user enter set number from 1 to 22
idx = int(val)
if idx >=1 and idx <= 22: 
  line = f.readlines()[idx-1].split()

  plier = line[0]#multiplier
  plicand = line[1]#multiplicand
  product = line[2]
  print("Let's prove that " + plier + " * " + plicand + " = " + product + ".\n" )
  division(plier, plicand, product)
  multiplication(plier,plicand,product)
  addition(plier, plicand, product)
  print("And there you have it! " + plier + " times " + plicand + " equals " + product)
else: print("Set not found")
f.close()
