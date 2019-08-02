cool_row,cool_col=map(int,input().split())
go=[]
for _ in rangecool_row):
    go.append(input())
for ic in range(len(go)):
    if('0' in go[ic]):
        go[ic]=go[ic].replace('0','')
        go[ic]=go[ic].replace(' ','')
lengths=[]
for ic in go:
    if(len(ic)>0):
        lengths.append(len(ic))
cool_col=min(lengths)
rt1='1 '*cool_col
rt1=rt1.strip()
for ic in range(cool_col):
    print(rt1)
