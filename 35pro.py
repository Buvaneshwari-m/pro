buvi=input()
pappa=len(buvi)
i=0
while(i<pappa):
    jii=0
    kee=0
    for j in range(len(buvi)):
        kee+=1
        if(buvi[i]==buvi[j]):
            if(kee>jii):
                jii=kee
            kee=0
        if(kee>pappa):
            break
    if(kee>jii):
        jii=kee
    if(jii<pappa):
        pappa=jii
    i+=1
print(pappa)
