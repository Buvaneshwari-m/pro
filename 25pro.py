def GORO(arrs,size):
    juli=[]
    count=1
    for i in range(0,size-1):
        if arrs[i]<arrs[i+1]:
            count+=1
        else:
            juli.append(count)
            count=1
    juli.append(count)
    print(max(juli))
size=int(input())
arrs=list(map(int,input().split()))
GORO(arrs,size)
