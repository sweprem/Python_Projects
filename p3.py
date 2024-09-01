#remove a string from a list
#IMP, we cannot remove a character from a string, we can do replace
list=['a\nd','sk\nlo','ko\nsop']
for i in list.copy():
       if i == 'sk\nlo':
        list.remove(i)
        print(list)


#new list is created to append with the chnages made
#remove newline character for a list
list=['a\nd','sk\nlo','ko\nsop']
output=[]
for i in list:
       output.append(i.replace('\n',' '))
print(output)

#to remove a single charcater from all strings in the list
#use of empty list to append
#or can use list[outerindex] and increment it
#str='' is given after for i loop , to empty the str after each i from list
list=['a\nd','sk\nlo','ko\nsop']
list1=[]
for i in list:
    str=''
    for j in i:
        if j == '\n':
            str+=''
        else:
            str+=j
    list1.append(str)
print(list1)

# to check whether an object is a list or not
#type([])=list is used to find the datatype
#list is not a keyword, a type,which changes dynamically
#list is used in other program ,it throws a bug.
list5=['2','3','4']
list6='234'
string="abc"
print("type of list",type(list5))
if type(list5) is type([]):
    print("list")
else:
    print(" not list")

#convert a string representation of list to list
list="[1,2,3,4,6]"
output=list.strip('][').split(',')
print(output)

#eval converts a string rep of list to actual list
list="[1,2,3,4,6]"
output=eval(list)
print(output)

#most frequent element in a list
#for loop to run
#list.count(i) to find the freq of that element in entire list
#if that freq is greater than count,assign it, assign the ele to a var

list=[1,3,2,4,3,2,4,3,3]
count=0
output=0
for i in list:
    freq=list.count(i)
    if(freq>count):
        count=freq
        output=i
print(output)

list=[1,3,2,4,3,2,4,3,3]
d={}
count=0
for key in list:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
        if d[key]>count:
            count=d[key]
            output=key
print(output)




