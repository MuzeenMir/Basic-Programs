from timeit import default_timer as timer
import random
ns = int(input('enter number of elements: '))
ls = int(input('enter start point: '))
le = int(input('enter end point: '))
a = str(ns)
len(a)
start = timer()
list = []
for m in range(ns):
    n = random.randint(ls,le)
    list.append(n)
a = len(list)
print(a)
print('unsortted: ', list)
temp = 0
newlist = []
while newlist != list:
    i = 0
    j = 1
    newlist = list[:]
    while i < a-1:
        if list[i]>list[j]:
            list[i], list[j] = list[j], list[i]
        i = i+1
        j = j+1
end = timer()
print(end - start)
print('sorted: ', list)
print('number of elements produced: ', a)
