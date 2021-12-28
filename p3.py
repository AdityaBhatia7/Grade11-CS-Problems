a,b=6,7
l=[2,4,5]
l.insert(1,7)
print(l)

n = int(input("enter a number: "))
lis = []
evenSum = 0
oddSum = 0
evenCount = 0
oddCount = 0
for i in range(n):
    num = int(input("enter elements of list: "))
    lis.append(num)
for j in lis:
    if j%2==0:
        evenSum += j
        evenCount += 1
    else:
        oddSum += j
        oddCount += 1
print()
print("sum of even numbers:",evenSum)
print("count of even numbers:",evenCount)
print("sum of odd numbers:",oddSum)
print("count of odd numbers:",oddCount)

l = [1,0,0,0,1,1,0,0,1]
count = 0
ln = []
for i in l:
  if i == 0:
    ln.append(i)
    count = len(ln)
    if count >= max:
      max = count
  else:
    ln = []
    count = 0
print(max)
