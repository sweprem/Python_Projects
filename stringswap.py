list=['man','women','baby']
print(list)
outeridx=0
for i in list:
  list[outeridx]=i.replace('a','e')
  outeridx+=1
print(list)
