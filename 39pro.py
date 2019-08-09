bu,l1=map(str,input().split())
panda=0
if len(bu)>len(l1):
  bu,l1=11,bu
lo1=0
while lo1<len(bu):
  panda+=(ord(l1[lo1])-ord(bu[lo1]))
  lo1+=1
for lo1 in range(lo1,len(l1)):
  panda+=ord(l1[lo1])-ord('a')+1
print(panda)
