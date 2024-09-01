list=[23,45,67]
print(list)
count=0
for i in list:
    sum=0
    for j in str(i):
        sum=sum+int(j)
    print(sum)


print("--------------------------------------------------")

list=[1,2,3,4]
mul=1
for i in list:
    mul=mul*i
print(mul)

print("--------------------------------------------------")



list=[4,3,7,0]
list.sort()
print("small no:",list[0])

print("--------------------------------------------------")

list=[4,3,7,0]
print("small no:",min(list))

print("--------------------------------------------------")

list=[4,3,7,0]
list.sort()
print("big no:",list[-1])

print("--------------------------------------------------")

list=[4,3,7,0]
list.sort()
print("second big no:",list[-2])

print("--------------------------------------------------")

list=[4,3,7,0]
print("big no:",max(list))

print("--------------------------------------------------")

list1=[]
for i in range(0,5):
    list=int(input("enter numbers:", ))
    list1.append(list)
print(list1)
print("the biggest no:", max(list1))

print("--------------------------------------------------")


