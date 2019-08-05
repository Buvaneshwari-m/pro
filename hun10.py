jb=input()
ju=input()
vg=input()
for i in vg:
    flag=0
    if( (i in ju) and (ju.count(i)==vg.count(i))):
        flag=1
if(flag==1):
    print("YES")
else:
    print("NO")
