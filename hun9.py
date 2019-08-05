hou=int(input())
polo=list(map(int,input().split()))
t=max(polo)
c,d=0,0
for i in range(0,len(polo)-1):
  for j in range(i+1,len(polo)):
    if abs(polo[i]+polo[j])<t:
      c,d=polo[i],polo[j]
      t=abs(c+d)
print(c,d)
