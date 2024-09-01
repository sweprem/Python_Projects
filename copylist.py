list=['happy','sad','angry']
emotions = list
print(emotions)

print("----------------------------------------")

list=['happy','sad','angry']
emotions = list[:]
print(emotions)
print("----------------------------------------")

import copy
list=['happy','sad','angry']
emotions = copy.copy(list)
print(emotions)

print("----------------------------------------")

list=['happy','sad','angry']
for i in list:
    newlist=list
print(list)
