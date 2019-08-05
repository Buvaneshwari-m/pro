outer=int(input())
io=list(map(int,input().split()))
for i in io:
    if io.count(i)>1:
        print(i)
        break
else:
    print("unique")
