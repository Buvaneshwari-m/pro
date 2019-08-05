lo1=int(input())
ji=list(map(int,input().split()[:lo1]))
for i in range(len(ji)):
    if((i%2==0)and(v[i]%2!=0)or(i%2!=0)and(v[i]%2==0)):
        print(v[i],end=" ")
