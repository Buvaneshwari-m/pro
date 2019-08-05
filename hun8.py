so=input()
hi=list(map(int,input().split()))
for i in range(len(hi)):
  for j in range(len(hi)):
    for k in range(len(hi)):
      if hi[i]+hi[j] == hi[k] and i<j<k:
        print(hi[i],hi[j],hi[k])
