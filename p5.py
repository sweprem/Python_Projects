#remove all the occurence of an element from list
list=[1,6,4,6,3,6,4,6,7]
for i in list.copy():
    if i == 6:
        list.remove(i)
print(list)

#find string from agiven substring
list=["chikkiboy","sun","moon","cutechikki"]
substring="chikki"
for i in list:
    if substring in i:
        print(i)

#sort a list of strings
list=["sun","earth","xoxo","apple"]
list.sort()
print(list)

#sort a list of strings in reverse order
list=["sun","earth","xoxo","apple"]
list.sort(reverse=True)
print(list)

#remove special character from string
string="su$near%thxox^oappl*e"
bad=['$','%','^','*']
for i in string:
    if i in bad:
     string.replace(i,'')
print(string)

#print odd nos
list=[1,2,3,4,5,6,7]
for i in list:
    if i%2!=0:
        print(i)

#print count of odd n even no in list
list=[1,2,3,4,5,6,7]
evencount=0
oddcount=0
for i in list:
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1
print(evencount)
print(oddcount)
print("-----------------------------------------------------------------------")

#to print random number
#for iteration of nos - values needed
#randrange - from 0 to 6
import random
for i in range(1,10):
    op=random.randrange(25)
    print(op)

#print all sublist of a list
list=[1,2,3]
sublist=[]
n=len(list)
for i in range(n):
    for j in range(i+1,n+1):
        sublist.append(list[i:j])
print(sublist)

#check if list is empty or not
list=[]
print(len(list))

#copy list
list=[1,2,3]
list1=list.copy()
print(list1)






