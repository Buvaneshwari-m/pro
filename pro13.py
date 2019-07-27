buvii, hos = [int(i) for i in input().split()]
vizh = []
Lis = [int(i) for i in input().split()]
for _ in range(hos):
    sav, gir = [int(i) for i in input().split()]
    vizh.append(min(Lis[sav-1:gir]))
for i in vizh:
    print(i)
