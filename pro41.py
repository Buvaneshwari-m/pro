mango,fru=input().split()
mango=int(mango)
fru=int(fru)
hack=''
rrr=2
if(mango+fru<=3):
    for i in range(0,mango+fru):
        if(i%2!=0):
            hack=hack+'0'
        else:
            hack=hack+'1'
else:    
    for i in range(0,mango+fru):
        if(i==rrr):
            hack=hack+'0'
            if(rrr==fru):
                rrr=rrr+2
            else:
                rrr=rrr+3
        else:
            hack=h+'1'
x=len(hack)-1
if(int(hack[x])==0):
    print('-1') 
elif mango==1 and fru==2: 
     print("011")
else:
    print(hack)
