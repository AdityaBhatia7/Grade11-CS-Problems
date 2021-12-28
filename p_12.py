lis = []
while 1==1:
  print("\n***CHOOSE YOUR OPTION***")
  print("1. Enter data for Sales Person \n2. Exit")
  selec = int(input())
  if selec == 1:
    while True:
      SalesID = input("Enter ID of sales person: ")
      if len(SalesID) == 0:
        break
      elif SalesID[0] != "S" or " " in SalesID:
        print("\\\Wrong format of ID//\n")
        break
      Name = input("Enter name of sales person: ")
      SalesMade = int(input("Enter amount of sales made: "))
      Comm = float(input("Enter amount of commision: "))
      print()
      lis.append([SalesID,Name,SalesMade,Comm])
    for i in lis:
      if i[3] >= 1000.0:
        print("Info of Sales Person with commision greater than 1000: ")
        print(i)
      #if int(list(i)[3]) >= 1000:
        #print(i)
  elif selec == 2:
    break
  else:
    print("\\\Invalid Input//\n")

while True:
    cont = input("do you want to continue?: ")
    if cont == "no":
        break
    else:
        list1 = list()
        list1.append(input("enter your name: "))
        list1.append(input("enter your percentage: "))
print(list1)
