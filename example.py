list =['car','bike','flight','truck']
print(list)
outeridx=0
##Manually replacing
for i in list:
    print(i)
    new_str=''
    for j in i:
        print(j)
        if(j=='i'):
            new_str+='e'
        else:
            new_str+=j
    list[outeridx]=new_str
    outeridx+=1

##Manually replacing
outeridx=0
for i in list:
    list[outeridx]=i.replace('i','e')
    outeridx+=1

print(list)















