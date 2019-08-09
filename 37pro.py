buvan=int(input())
jo=list(map(int,input().split()))
teddy=0
sss=0
while(sss<len(jo)):
    tat=jo[sss]
    if(sss==0):
        if(len(jo)==1):
            teddy=1 
            break
    elif(sss==len(jo)-1):
        teddy=teddy
    else:
        if(tat>jo[sss+1] and tat>jo[sss-1]):
            teddy=teddy+1
        elif(tat<jo[sss-1] and tat<jo[sss+1]):
            teddy=teddy+1
    sss=sss+1
print(teddy)

