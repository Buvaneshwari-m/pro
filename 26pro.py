dad=int(input())
now=list(map(int,input().split()))
are=[]
pr=1
for i in now:
  if i not in are:
    are.append(i)
for i in range(len(are)-1):
  if (are[i]<are[i+1]):
    pr+=1
print(pr)
