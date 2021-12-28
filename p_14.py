s=input("Enter a number")
print("MENU")
print("1.Prime Number")
print("2.Armstrong Number")
print("3. Palindrome")
while True:
    ch=int(input("Enter choice"))
    if ch==1:

else if ch==2:
  l=list(s)
  s1=0
  for i in l:
    s1=s1+i**3
            if s==s1:
                print("Armstrong")
            else:
                print("Not Armstrong")
            

    else if ch==3:
        r=s[::-1]
        if s==r:
            print("Palindrome")
        else:
            print("Not a Palindrome")
    else:
        break
        
s = input("enter a string: ")
l = list(s)
length = len(l)
index = -1
for i in range(length-1, int(length/2), -1):
     
        if l[i].isalpha():
            temp = l[i]
            while True:
                index += 1
                if l[index].isalpha():
                    l[i] = l[index]
                    l[index] = temp
                    break
