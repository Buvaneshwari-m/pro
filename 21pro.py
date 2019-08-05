import statistics as studio
count1=int(input())
course=list(map(int,input().split()))
hint=False
for i in range(1,count1):
    l1=course[:i]
    l2=course[i:]
    if studio.mean(l1)==studio.mean(l2):
        hint=True
if hint==True:
    print("yes")
else:
    print("no")
