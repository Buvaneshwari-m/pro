import math
ko2,l2=map(int,input().split())
beach2=[]
k2=list(map(int,input().split()))
for j in range(0,l2):
    auro2,hin2=map(int,input().split())
    beach2.append([auro2,hin2])
for j in beach2:
    hh2=j[0]-1
    zz2=j[1]-1
    print(math.gcd(k2[hh2],k2[zz2]))
