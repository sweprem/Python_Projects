#max of two nos
a=1
b=4
if (a>b):
    print(a)
else:
    print(b)

print("----------------------------------------------------------------------------------")
#create a list with given length
list=[1]*5
print(list)

#above with another method
list=[]
n=len(list)
n=3
for i in range(0,n):
 list.append(0)
print(list)

print("----------------------------------------------------------------------------------")
# create a list given a range
start=1
end=10
list=[]
for i in range(start,end+1):
    list.append(i)
print(list)

print("----------------------------------------------------------------------------------")
# create a list given a range
list=[*range(10,20,1)]
print(list)

print("----------------------------------------------------------------------------------")

#first and last elements of a list
list=[1,4,5,8,9]
print(list[0])
print(list[-1])

print("----------------------------------------------------------------------------------")

#convert set to list
set={1,2,3}
list=[i for i in set]
print(list)
#convert set to list
set={1,2,3}
list=[]
for i in set:
    list.append(i)
print(list)
print("----------------------------------------------------------------------------------")

##create dictionary of lists
#create a empty dictionary
#create lists within dic and assign values
dic={}
dic["name"]=['miky','kitty']
dic["number"]=['123','345','454']
print(dic)
print("----------------------------------------------------------------------------------")

##create a sublist for list in dic

dic={}
dic["name"]=['miky','kitty']
othername=['vicky','docky']
dic["name"].append(othername)
print(dic)

print("----------------------------------------------------------------------------------")

##remove first element in list
list=[8,4,3,2]
list.remove(list[0])
print(list)

print("----------------------------------------------------------------------------------")

##interchange first and last elements of list
list=[1,2,3,4,5]
list[0],list[-1]=list[-1],list[0]
print(list)

print("----------------------------------------------------------------------------------")

#swap two elements in list
list=[1,2,3,4,5]
temp=0
temp=list[1]
list[1]=list[2]
list[2]=temp
print(list)

print("----------------------------------------------------------------------------------")

##remove multiple elements from list
#create a list to delete elements
#use copy() in for -- wecannot delete on iterating list which changes its indexes after 1st deletion
list=[1,2,3,4,5]
waste=[2,3,4]
for i in list.copy():
 if i in waste:
     list.remove(i)
print(list)

print("----------------------------------------------------------------------------------")

#second largest element in list
list=[6,4,8,4,2]
list.sort()
print(list)
print(list[-2])

print("----------------------------------------------------------------------------------")

## occurence of a element in a list
list=[1,2,4,5,2,5,2,4]
count=0
for i in list:
    if i==2:
        count=count+1
print(count)

print("----------------------------------------------------------------------------------")
## occurence of ALL element in a list
#create dictionary for unique  key and its frequency- dic hetero value
#when list is used it cant be achived since it holds homo data or it prints every ele n frequency without beong unique
list=[1,2,4,5,2,5,2,4]
d={}
for key in list:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
print(d)

print("----------------------------------------------------------------------------------")

#intersection of two list
list1=[1,2,3,4]
list2=[3,4,5,6]
list3=[i for i in list1 if i in list2]
print(list3)

list1=[1,2,3,4]
list2=[3,4,5,6]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)

print("----------------------------------------------------------------------------------")


