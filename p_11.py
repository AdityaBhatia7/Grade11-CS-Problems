a = input('enter string = ')
i = 0
new = a.split()
b = len(new)
print(b)
print(new[i])
c = len(new[i])
print(c)
count = 0
while i <= b:
  if c <= 4:
    print('yes')
    count += 1
  c += 1
  i+=1
print('no. of words with length <=4 = ',count)

days = int(input("enter number of days: ")
fine = 0
while days > 10:
    fine += 80
    days -=1
while days > 5 and days <= 10:
    fine += 65
    days -= 1
while days > 0 and days <= 5:
    fine += 40
    days -= 1
print("amount in rupees is: ", fine/100)
