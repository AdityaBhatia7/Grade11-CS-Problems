a = input('enter string: ')
i,flag = 0,0
j = len(a)-1
while i <= j:
  if a[i] != a[j]:
      flag = 1
      break
  i += 1
  j -= 1
if flag == 1 :
    print(a,'is not a palindrome')
else :
    print(a,"is a palindrome")
    
x = int(input('enter base: '))
n = int(input('enter power: '))
print('1',end = " ")
count = 1
while count < n+1 : 
  a = x**count
  print(a,end = " ")
  count = count + 1
