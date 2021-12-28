string = input('enter string = ')
vowels = 'aeiouAEIOU'
v,c=0,0
for i in string:
  for j in vowels:
    if i == j:
      v += 1
print('no. of vowels = ',v)
print('no. of consonants = ',len(string)-v)

string = input('enter string: ')
a1,e1,i1,o1,u1 = 0,0,0,0,0
for i in string :
  if i == 'a' or i=='A' :
    a1 += 1
  elif i == 'e' or i=='E' :
    e1 += 1
  elif i == 'i' or i=='I' :
    i1 += 1
  elif i == 'o' or i=='O' :
    o1 += 1
  elif i == 'u' or i=='U' :
    u1 += 1
print('no. of a = ',a1)
print('no. of e = ',e1)
print('no. of i = ',i1)
print('no. of o = ',o1)
print('no. of u = ',u1)
