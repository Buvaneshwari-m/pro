buvs1=int(input())
array=[]
jj=[]
for o in range(buvs1):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        jj.append(num)
jj.sort()
for o in jj:
    print(o,end=' ')

