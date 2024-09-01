list=[-1,0,7,-3]
for i in list:
    if (i>=0):
     print("positive nos:", i)
    else:
     print("negative nos:",i)

print("---------------------------------------")

list=[-1,0,7,-3]
n=len(list)
print(n)
num=0
while(num<n):
    if list[num] >= 0:
        print("pos:", list[num])
    num+=1

print("---------------------------------------")

start,end=1,10
for i in range(start,end+1):
    if i>=0:
        print("pos nos in range:",i)

print("---------------------------------------")

start,end=-5,5
count=0
negcount=0
for i in range(start,end+1):
    if i>=0:
        count=count+1
    else:
        negcount=negcount+1
print("pos count:",count)
print("neg count:",negcount)

print("---------------------------------------")

list1=[]
for i in range(1,5):
    list=int(input("enter the nos"))
    list1.append(list)
print(list1)
count=0
for i in list1:
    if i>=0:
        count=count+1
print("pos:",count)



