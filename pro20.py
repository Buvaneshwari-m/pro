road,tree=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
kee=0
total=tree
for z in arr:
    if total>=z:
        rem=int(total/z)
        kee+=rem
        total=total - (i*rem)
    if total==0:
        break
if total==0:
    print(kee)
else:
    print("it's not possible to sum up coins in such a way that they um upto",tree)
