#convert number to list of integer
#convert to string first so we can use for loop
#int(i) needed in int in list
num=1234
list=[int(i) for i in str(num)]
print(list)

# remove None from list
#list.copy() for iteration , we cant remove n iterate from same

list=[1,None,4,None]
for i in list.copy():
    if i == None:
        list.remove(i)
print(list)

#append at beginning of list
list=[3,4,6,7]
list.insert(0,1)
print(list)

#index and value
list=[3,4,6,7]
for i in range(0,len(list)):
 print(i,list[i])

#check if lists are same
list1=[3,4,6,7]
list2=[3,4,6,8]
if list1 == list2:
    print("same")
else:
     print("not same")

#last element of list
list1=[3,4,6,7]
print(list[-1])

#clear list
list1=[3,4,6,7]
print(list1)
list1.clear()
print(list1)

#even nos in a list
list5=[3,4,6,7]
for i in list5:
    if i%2==0:
        print(i)


#smallest no in a list
#assign first element as mini
#use for in range for iteration to compare with every element
#if <min satisfies, assign that value to mini, repeat
list=[6,7,8,3,7]
min=list[0]
for i in range(0,len(list)):
   if list[i]<min:
       min=list[i]
print(min)

#split a list into multiple lists
list=[1,2,3,4,5,6,7,8,9]
for i in range(0,len(list),3): #(start, end,step)
    print(list[i:i+3]) #to print list[] in i and i+3 elements

#append string to alist
#a list can contain any type of data
list=[6,7,8,3,7]
list.append("heelo")
print(list)

#get last N elements from a list
#-n : prints last 3 elements
list=[6,7,8,3,7]
n=3
print("last n ele",list[-n: ])

#get last N elements from a list
#reverse the list
#append last 3 ele in new list using while
#reverse the new list again to get in same order as first
list=[6,7,8,3,7]
list1=[]
list2=list[ ::-1]
print(list2)
i=0
while(i<3):
    list1.append(list2[i])
    i+=1
list1.reverse()
print(list1)

#element present in string
#we have split the string first making it i
#for every i and j compare , put flag to print at the end

sen="i am chikki kutty boy"
list=['chikki','bo']
sen=sen.split(" ")
flag=0
for i in sen:
    for j in list:
        if i==j:
         flag=1
if flag==1:
    print('yeah')
else:
    print('no')

#split a sentence into list of words
sen="i am chikki kutty boy"
list=[]
sen=sen.split()
for i in sen:
    list.append(i)
print(list)

#muli=dim list
#a list can have multiple sub lists within them , use of dic is best
list=[[1,2],[3,4],[5,6]]
for i in list:
    print(i)

#empty string from a list of strings
list=[" ","hi"," ","hello"," "]
for i in list.copy():
    if i==" ":
        list.remove(i)
print(list)

#list of integers to single integer
list=[1,2,3,4,5]
integer=''
for i in list:
    integer=integer+str(i)
print(int(integer))

#even nos in a range
start=1
end=10
list=[]
for i in range(start,end+1):
    if i%2==0:
        list.append(i)
print(list)

#sort a list of tuples by 2nd item
#sort it using key and item by item[1] =second item
input=[('oinky',8),('pinky',9),('dolly',6),('moky',2)]
input.sort(key=lambda i:i[1])
print(input)

#dup from alist of integers
list=[2,7,4,2,5,4,8,4]
uniq=[]
dup=[]
for i in list:
    if i not in uniq:
        uniq.append(i)
    elif i not in dup:
        dup.append(i)
print(dup)

#common element in two list
list1=[3,4,5,6,7]
list2=[1,2,3,4,5]
for i in list1:
    for j in list2:
        if i==j:
            print(i)

#sort by 2nd element in sublist
list=[[1,'d'],[4,'c'],[8,'a'],[7,'b']]
list.sort(key=lambda i:i[1])
print(list)


#convert a list of char to string
list=['h','e','l','l','o']
string=""
for i in list:
    string =string+i
print(string)





