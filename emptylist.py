## remove empty list

list=[1,2,3,[],4,5,[],[],7,8]
print(list)
for i in list.copy():
    if i==[] :
        list.remove(i)
print(list)
