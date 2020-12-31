#This program determines which set of numbers 
#work with the Abbott Costello DMA Proof Trick

#This trick involves multiplying two factors 
#to get the wrong product and proving that calculation
#is correct through division, multiplication and addition
#For example, 7 * 13 = 28 instead of 91

#Assumptions:
#1) The multiplier is a 1 digit number(between 1 and 9)
#2) The multiplicand and product are 2 digit numbers
#(between 10 and 99)

#Creates a text file containing all posible combos
#Each line has 2 factors and a product 
#f = open("combos.txt", "w")
#for plier in range(1,10):
 # for plicand in range(10,100):
  #  for product in range(10,100):
   #   f.write(str(plier) + " " + str(plicand) +  " " + str(product) + "\n")
#f.close()

#This function saves the sets that 
#work with the trick in a new file
def write_working_combos(plier, plicand, product):
  f = open("workingCombos.txt", "a")
  f.write(plier + " " + plicand + " " + product + "\n")
  f.close()

#open and read the file
f = open("combos.txt", "r")
for  l in f:
  #separate the line by spaces
  line = l.split()
  #save contents into variables
  #The trick is written in the following format:
  #a * mn = xy
  a = int(line[0])#multiplier
  mn = line[1]#multiplicand
  xy = line[2]#product
  m = int(line[1][0])#multiplicand's tens place
  n = int(line[1][1])#multiplicand's ones place
  x = int(line[2][0])#product's tens place
  y = int(line[2][1])#product's one place

  #The set of numbers must satisfy 3 conditions:
  #For division:
  #1) y/a = m
  #2)(10x + r)/a = n, where r = y mod a
  #For multiplication/addition:
  #3) a(m*n) = xy
  
  if ((y//a) == m) and ((10*x + y % a)//a == n) and (a*(m+n) == 10*x + y):
    write_working_combos(str(a),mn,xy)
