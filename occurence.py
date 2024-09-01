list=['wall','wheel','wall','wall','wheel']
print(list)
count=0
for i in list:
    if (i== 'wall'):
        count=count+1
print(count)

print('--------------------------------------------------')

list=[2,3,4,5,6,7,8,8]
sum=0
for i in list:
    sum=sum+i
print(sum)
avg=0
avg=sum/len(list)
print(avg)

print('--------------------------------------------------')


import numpy as np
list=[2,3,4,5,6,7,8,8]
sum=np.sum(list)
avg=np.average(list)
print(sum)
print(average)
