jo = int(input())
buvi= [ int(i) for i in input().split()]
jo = len(buvi)
huu= 0
for Xtee in range(0,jo-2):
    for Ytee in range(Xtee+1, jo-1):
        for Ztee in range(Ytee+1, jo):
            if buvi[Xtee] > buvi[Ytee] > buvi[Ztee] :
                huu =huu+ 1
print(huu)
