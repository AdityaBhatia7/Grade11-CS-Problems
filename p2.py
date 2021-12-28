dict = {'1':'a', '2':'b'}
for k,v in dict.items():
    print(k,v)
    
sf=""
while true:
    s = input("enter a character: ")
    if s != "#":
        sf += s
    else:
        break
count = 0
for i in sf:
    if i == " ":
        count += 1
print("no of words:", count)
