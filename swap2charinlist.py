list=['monkey','donkey','pinky']
print(len(list))
total=0
for i in list:
 total=total+1
print(total)

newlist=[i.replace('o',' ').replace('e','o').replace(' ','e') for i in list]
print(newlist)
