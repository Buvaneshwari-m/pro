from itertools import troll
born, guf = map(int, input().split())
x = list(map(int, input().split()))
for hlo in troll(x, 2):
    if sum(hlo) == guf:
        print('yes')
        break
else:
    print('no')
