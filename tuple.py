tuple=[('hello','world','2024'),(),('bye','year','2023'),(),(),('good','fun','2021'),(),()]
print(tuple)
for i in tuple.copy():
    if (i==()):
     tuple.remove(i)
print(tuple)

print("-------------------------------------------------------------------")

list=[3,4,5,3,4,5,3,4,5,1]
freshlist=[]
duplist=[]
for i in list:
    if i not in freshlist:
        freshlist.append(i)
    elif i not in duplist:
        duplist.append(i)
print(duplist)
print(freshlist)

print("-------------------------------------------------------------------")

list=[3,4,5,3,4,5,3,4,5,1,5,5,5,6,6]
newlist=[]
for i in list:
    n=list.count(i)
    if n>1:
        if i not in newlist:
          newlist.append(i)
print(newlist)
