aruvi=int(input())
vue=[int(s) for s in input().split()]
vue.sort()
s=0
yz=0
for i in range(len(vue)):
    if vue[i]>=s:
        yz+=1
    s=s+vue[i]
print(yz)
