import random
from timeit import default_timer as timer

a = int(input('enter the list size: '))
b = int(input('enter the starting number: '))
c = int(input('enter the ending number: '))

def mergeSort(l, s):
    listx = []
    y = 0

    if a%2 != 0:
        listx.append([l[y],l[y+1],l[y+2]])
        y = 3    
        for i in range(s-1):
            listx.append([l[y], l[y+1]])
            y = y+2
            if s == y:
                break
        #print('broken down list: ', listx)
        
    else:
        m = 0
        for i in range(s-1):
            listx.append([l[m], l[m+1]])
            m = m+2
            if s == m:
                break
#        print('broken down list: ', listx)
    l = 0
    while len(listx) > 1:
            final_list = []        
            for i in range(0, len(listx)-1, 2):
                final_list.append(listx[i] + listx[i+1])
                final_list[-1].sort()
                global z
                z +=1
            if len(listx) % 2 != 0:
                final_list.append(listx[-1])
                final_list.sort()
            listx = final_list
    print(listx)

z = 0
list = []
for i in range(a):
    x = random.randint(b,c)
    list.append(x)
print('unsorted list: ', list)
o = len(list)

if b < c:
    start = timer()
    mergeSort(list, a)
    end = timer()
    print('time elapsed is: ', end - start)
    print(z)
else:
    print('some error occured!')
