list = [1, 2, 3, 4, 5, 6]
for i in list:
    if i % 2 == 0:
        list.remove(i)
print(list)

print("===============================")

list = [1, 2, 3, 4, 5, 6]
del list[1:2]
print(list)

print("===============================")

list = [1, 2, 3, 4, 5, 6, 7, 8]
delete = [1, 2, 3]
for i in sorted(delete, reverse=True):
    del list[i]
print(list)

print("===============================")

list = [8, 7, 5, 3]
for i in list:
    if (i<=5):
     print(i)

print("===============================")

