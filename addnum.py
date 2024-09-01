a=5
b=10
if (a<b) :
    print(a)
else:
    print(b)
print("---------------------------------------------------")
a=10
b=18
small=min(a,b)
print(small)
print("-------------------------------------------------------")

list=['chikki','amma','appa']
for i in list:
 if (i=='chikk'):
   print('found')
 else:
     print('not found')

print("----------------------------------------")

list=[1,3,6,7,8,9]
print(list)
list.clear()
print(list)

print("------------------------------------")
list1=[1,3,6,7,8,9]
list2=[1,4,6,7,8,9]
print(list1)
print(list2)
del list1[:]
del list2[:]
print(list1)
print(list2)

print("------------------------------------")
listold=[1,3,6,7,8,9]
print(listold)
listnew=listold[::-1]
print(listnew)

print("------------------------------------")
list=[1,3,6,7,8,9]
print(list)
list.reverse()
print(list)

print("------------------------------------")



