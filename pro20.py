jo_coin,sub_coin=list(map(int,input().split()))
oot_coin=list(map(int,input().split()))
oot_coin.sort(reverse=True)
io=0
for i in oot_coin:
    if sub_coin==0:
        break
    qt=sub_coin // i
    io+=qt
    sub_coin=sub_coin-i*qt
print(io)
