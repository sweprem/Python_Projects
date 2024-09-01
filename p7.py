#unique combinations of two lists:
#use (())- two parenthsesis - since append accepets only 1 argument
from collections import OrderedDict
list1=[1,2,3,2]
list2=[3,4,5]
list3=[]
unilist3=[]
uni=[]
for i in list1:
    for j in list2:
        list3.append((i,j))
print(list3) #has all poss combinations
unilist3=list(set(list3)) #to get unique combo, convert list to set , then set to list-- not ordered
uni=list(OrderedDict.fromkeys(list3)) # to get the same , by preserving thr order
print(unilist3)
print(uni)

#list of integer to list of strings
list=[2,3,4,5]
stringlist=[]
for i in list:
    stringlist.append(str(i))
print(stringlist)

#remove square bracket from list
#use join ,with , to move elements ,removing brackets
list=[3,5,7]
output=','.join(str(i) for i in list)
print(output)

#replace substring in a list of strings
list=["hello","hihe","hewh"]
for i in list:
    list=i.replace("he","oo")
    print(list)

#first element of each sublist
list=[[1,2],[1,3],[1,4]]
output=[]
for i in list:
    output.append(i[0])
print(output)

#build a matrix
rows=2
cols=2
matrix=[[0 for _ in range(cols)] for _ in range(rows)]
print(matrix)
matrix[0][0],matrix[0][1]=7,8
matrix[1][0],matrix[1][1]=5,6
print(matrix)

#merge list elements
#join() - to join
#the index takes element 'he'
list=['h','e','l','l','o']
list[0:2]=[''.join(list[0:2])] #replaces the 0,1 alone in the original list, so range is given in left and full[] in right
print(list)

#remove all elements in a list present in other list
list1=[5,6,7,8,9]
list2=[3,4,5,6,7]
for i in list1.copy():
 if i in list2:
     list1.remove(i)
print(list1)

#check if a list is subset of other list
list1=[1,2,3,4,5]
list2=[2,3,7]
flag=0
for i in list2:
    if i in list1:
      flag=1
    else:
        flag=0
if flag == 1:
    print("subset")
if flag == 0:
    print(" not subset")

#add two list elements
list1=[1,2,3]
list2=[1,2,3]
list3=[]
for i in range(0,len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)








