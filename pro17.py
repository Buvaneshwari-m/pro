ro_17=list(map(int,input().split()))
uut1=ro_17[1]
flag1=0
uu_17=list(map(int,input().split()))
for i in range(0,len(uu_17)-1):
	for j in range(i+1,len(uu_17)):
		if uu_17[i]+uu_17[j]==uut1:
			print("yes")
			flag1=1
			break
	if flag1==1:
		break
if flag1!=1:
	print("no")
