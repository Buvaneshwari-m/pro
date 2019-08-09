sathya1=input()
for ii in range(len(sathya1)):
  if(sathya1[ii] < sathya1[ii+1]):
    print(sathya1[ii+1:])
    break
