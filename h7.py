auro=input()
flo=list(map(int,input().split()))
for i in range(len(flo)):
  if (i%2 == 0 and flo[i]%2 !=0) or (i%2!=0 and flo[i]%2 == 0):
    print(flo[i],end= " ")
