days=int(input("enter no of days: "))
fine = 4
tfine = 0
count = 0
while days>0:
  if count >= 5:
    fine = 6
  elif count >= 10:
    fine = 8
  tfine += fine
  days-=1
  count+=1
print(tfine)

n=int(input("enter a number: "))
m=int(input("enter another number: "))
for i in range(n+1,m):    
    for j in range(1,11):        
        print(i,"×",j,"=",i*j)   
    print()
    
    n=int(input("enter a number: "))
m=int(input("enter another number: "))
flag = 1
for i in range(n+1,m):
  for j in range(2,i//2+1):
    if i%j==0:
      flag = 0
    else:
      flag = 1

  if flag==1:
    print(i)
