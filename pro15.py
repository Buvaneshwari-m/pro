romeo=input()
juliet=map(int,input().split())
park=[]
for i in juliet:
    got=bin(i)
    park.append(got)
hide=sorted(park)
hide.reverse()
for gg in hide:
    print(int(gg,2))
