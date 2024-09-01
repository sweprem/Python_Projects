list=[24,67,45]
print(list)
for i in list:
    if (i%2==0):
        print('even', [i])
    else:
        print('odd',[i])


print("--------------------------------------------")

start=int(input("enter start value"))
end=int(input("enter end value"))
for i in range(start,end+1):
    if(i%2!=0):
     print("odd nos in the given range:",i)

print("--------------------------------------------")

start=int(input("enter start value"))
end=int(input("enter end value"))
for i in range(start,end+1):
    if(i%2==0):
     print("even nos in the given range:",i)
    else:
     print("odd nos in the given range:",i)


