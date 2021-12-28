n = int(input('enter no: '))
sum , prod = 0 , 1
for i in range(1,n+1,1):
  print(i)
  sum = sum + i
  prod = prod * i
print('sum = ',sum , 'prod = ',prod)  
print('\n')
i = 1
sum,prod=0,1
while i < n+1 :
  print(i)
  sum += i
  prod *= i
  i += 1 
print('sum = ',sum , 'prod = ',prod) 

n=int(input("enter a number: "))
a1 = 1
a2 = 2
num = 1
sum = 0
pro = 1
for count in range(0,5):
  print(num)
  sum+=num
  pro*=num
  a1=a2
  a2=num
  num = a1+a2
print(sum, pro)
