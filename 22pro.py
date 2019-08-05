gova=int(input())
arise=list(map(int,input().split()))
arise.sort(reverse=True)
#print(arise)
sum=0
sum1=0
aro=[]
for i in range(0,gova,2):
    sum=sum+arise[i]
for j in range(1,gova,2):
    sum1=sum1+arise[j]
aro.append([sum,sum1])
#print(aro)
for i in aro:
    print(i[0] if i[0]>i[1] else i[1])
