kora1 = int(input())
juice = []
for i in range(pow(2, kora1)):
    juice.append(bin(i)[2:].zfill(kora1))
juice.sort(key=(lambda x: x.count('1')))
for i in juice:
    print(i) 
