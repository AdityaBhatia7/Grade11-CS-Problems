n=int(input("enter a number: "))
for i in range(1,n+1):
  for j in range(0,i):
    print("*", sep=" ", end="")
  print()
print()

for i in range(1,n+1):
  for j in range(0,(n+1)-i):
    print("*", sep=" ", end="")
  print()
  
  n = int(input('enter no. = '))
sum,prod=0,1
for i in range(2,2*n+1,2) :
  print(i)
  sum = sum + i 
  prod *= i 
print('sum = ',sum , 'prod = ',prod) 
print('\n')
i = 2
sum,prod=0,1
while i < 2*n+1:
  print(i)
  sum = sum + i 
  prod *= i 
  i += 2
print('sum = ',sum , 'prod = ',prod)  
