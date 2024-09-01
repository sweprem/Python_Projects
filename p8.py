#unzip tuples from list
tuples=[('happy',10),('sad',7),('good',9)]
list=[]
list1=[]
for i in tuples:
    list.append(i[0])
    list1.append(i[1])
print(list)
print(list1)

# to find N largest elements in list
list=[7,9,4,8,5]
list.sort()
print(list)
print(list[-3:])

#generate all valid IP address from a string
string="123457543"
