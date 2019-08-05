lo,hu=map(int,input().split())

pr=list(map(int,input().split()))

vr=list(map(int,input().split()))

g=[]

cr=0

for i in range(lo):

    xr=vr[i]/pr[i]

    g.append(xr)

while hu>=0 and len(g)>0:

    mindex=g.index(max(g))

    if hu>=pr[mindex]:

        cr=cr+vr[mindex]

        hu=hu-pr[mindex]

    pr.pop(mindex)

    vr.pop(mindex)

    g.pop(mindex)

print(cr)
