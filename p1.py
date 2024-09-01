#convert a list to tuple

#create alist
#use tuple(list) to convert a list to tuple
#print the stored variable

list=[1,2,3,4,5]
output=tuple(list)
print(output)

print("---------------------------------------------------------------------------------------------------------------")
####convert a list to string--move all elements of list to a variable

#create a list
#for string create a empty variable
#use for loop to move all elements of list to string
#str[i] is used since str concatenates with string ,not integer
#print the variable created for string

list=[1,2,3,4,5]
string=""
for i in list:
    string=string+str(i)
print(string)
print("---------------------------------------------------------------------------------------------------------------")

#join can be used for string of lists only
#''.join indicates whatever u put'' is joined, ',' - prints1,2, so on

list=[1,2,3,4,5]
print(' '.join([str(i) for i in list]))

print("---------------------------------------------------------------------------------------------------------------")


####to convert all strings in list to int-----

#create a list with strings
#provide a range for both list, one to create, other to iterate
#rnage is important for list creation , conversion
#IMP- only an integer stored as char'7' can be converted to int, not a character 'h'


list=["8","1","3"]
print(list)
n=len(list)
for i in range(0,n):
    list[i]=int(list[i])
print(list)
print("---------------------------------------------------------------------------------------------------------------")


####to convert all strings in list to int
list=["7","9","3"]
print(list)
list=[int(i) for i in list]
print(list)
print("---------------------------------------------------------------------------------------------------------------")


##another way - create a list,append it for range because the value doesnt know where to store

list=["8","1","3"]
print(list)
list1=[]
for i in list:
 list1.append(int(i))
print(list1)
print("---------------------------------------------------------------------------------------------------------------")


#remove duplicates from list

#create two empty lists
#run for loop to iterate elements
# use IF i NOT IN to check if the element in fresh list ,then append
#else move to dup list
#this way - the fresh list has originals removing duplicates

list=[2,3,4,2,4,5,3]
freshlist=[]
duplist=[]
for i in list:
    if i not in freshlist:
        freshlist.append(i)
    elif i not in duplist:
        duplist.append(i)
print(freshlist)

print("---------------------------------------------------------------------------------------------------------------")


###merge two diff list
#create a empty list for merge
#just use + for merging

list1=[2,3,4,5]
list2=[5,6,4,8]
list3=[]
list3=list1+list2
print(list3)

print("---------------------------------------------------------------------------------------------------------------")

#merge two list using* operand

list1=[2,3,4,5]
list2=[5,6,4,8]
list3=[*list1,*list2]
print(list3)

print("---------------------------------------------------------------------------------------------------------------")

#merge two list using append

list1=[2,3,4,5]
list2=[5,6,4,8]
for i in list2:
    list1.append(i)
print(list1)
print("---------------------------------------------------------------------------------------------------------------")

#iterate over a list - using for
# for - i refers to the element itself
#because in list -syntax
list=[7,8,9]
for i in list:
    print(i)
print("---------------------------------------------------------------------------------------------------------------")



#iterate using while loop
#in while loop i refers to index because of condion(i<n)
#so print list[i]- element
list=[7,8,9]
i=0
while i < len(list):
    print(list[i])
    i+=1
print("---------------------------------------------------------------------------------------------------------------")

#check element exists in list
list=[1,2,3,4,5]
for i in list:
    if i == 3:
     print("present")

print("---------------------------------------------------------------------------------------------------------------")
#check element existence -another way
list=[1,2,3,4,5]
i =4
if i in list:
 print("yes")

print("---------------------------------------------------------------------------------------------------------------")

#sum of elements in list
list=[1,2,3,4,5]
sum=0
for i in list:
    sum=sum+i
print(sum)

print("---------------------------------------------------------------------------------------------------------------")


#find largest number in the list
#sort ascending
#[-1] gives the largest no in list
list=[5,6,9,2,5]
list.sort()
print(list[-1])

#use of max for above
list=[5,6,9,2,5]
print(max(list))
print("---------------------------------------------------------------------------------------------------------------")

#mul all elements in list
list=[1,2,3,4]
mul=1
for i in list:
    mul=mul*i
print(mul)

print("---------------------------------------------------------------------------------------------------------------")

#unique value from list
list=[3,2,4,3,2,5,6,9,2]
uniqlist=[]
for i in list:
    if i not in uniqlist:
        uniqlist.append(i)
print(uniqlist)

print("---------------------------------------------------------------------------------------------------------------")

#one string to list of characters
string ="hello my dear"
output=[i for i in string]
print(output)

print("---------------------------------------------------------------------------------------------------------------")

#reversing a list
list=[1,2,3,4,5,6]
n=len(list)
list1=[]
for i in range(1,n+1):
 list1.append(list[n-i])
print(list1)

print("---------------------------------------------------------------------------------------------------------------")

#average of a list
list=[1,2,3]
sum=0
avg=0
n=len(list)
for i in list:
    sum=sum+i
print(sum)
avg=sum/n
print(avg)
print("=========================================================================================")
#list as input from the user
#create an empty list
#set the range
#iterate using for loop
#input the value in int
#store the values in a variable
#append it to list
list=[]
for i in range(0,5):
    value=int(input("enter the values:", ))
    list.append(value)
print(list)

print("=========================================================================================")


