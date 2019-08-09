bea1="vir"
bea2=input()
co1=list(set(bea1)-set(bea2))
co2=list(set(bea2)-set(bea1))
co=len(co1)+len(co2)
if co==0:
	print("yes")
else:
	print("no")
