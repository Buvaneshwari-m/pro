hue=int(input())
io1=2**hue
list1=[]
for i in range(0,io1):
    l=bin(i)[2:].zfill(hue)
    if(len(l)<len(bin(2**hue-1)[2:])):
        list1.append([l.count("1"),l])
    else:
        list1.append([l.count("1"),l])
list1.sort()
for i in range(len(list1)):
    print(list1[i][1])
