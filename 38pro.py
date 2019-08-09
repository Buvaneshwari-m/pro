buv,jo=map(int,input().split())
ros=list(map(int,input().split()))
tear=0
for Xt in ros:
    if Xt<=(5-jo):
        tear+=1
otee=tear//3
print(otee)
