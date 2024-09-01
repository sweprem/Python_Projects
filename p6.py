#max and mini element position in list
#index 0 to n-1
#postion 0 to n
list=[1,5,3]
min=list[0]
max=list[0]
for i in range(1,len(list)):
    if i > max:
        max=i
    if i< min:
        min=i
print(max)
print(min)

# union of list
list1=[1,2]
list2=[3,4]
list3=[]
list3=list1+list2
print(list3)

#sort based on length

list=['anuhuihuihuhhdk','jwdhwudh','hhgq']
list.sort(key=len)
print(list)

#select randam n elements from a list:
#random.sample() means we need to give from what-and :list , how many-5 elements
import random
list=[7,9,3,2,1,9,32,33]
list1=[]
list1=random.sample(list,5)
print(list1)


