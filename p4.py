age=int(input("enter your age: "))
if age < 13:
  print("you are a child")
elif age >= 13 and age <= 19:
  print("you are a teen") 
elif age >= 20 and age <= 40:
  print("you are a young adult") 
elif age >= 41 and age <= 60:
  print("you are middle aged")
elif age >= 61 and age <= 80:
  print("you are a senior citizen")
else:
  print("you are a super citizen")
  
  n=input("enter a character: ")
if n.islower() == True:
  print("character is lower case")
elif n.isupper() == True:
  print("character is upper case")
elif n.isnumeric() == True:
  print("character is a digit")
elif not n.isalnum() == True:
  print("character is a special char")
  
  n=int(input("enter a number: "))
m=int(input("enter another number: "))
o=int(input("choose an operator:\n1. +\n2. -\n3. *\n4. /\n"))
if o == 1:
  print(n+m)
elif o == 2:
  if n>m:
    print(n-m)
  else:
    print(m-n)
elif o == 3:
  print(n*m)
elif o == 4:
  if m != 0:
    print(n/m)
