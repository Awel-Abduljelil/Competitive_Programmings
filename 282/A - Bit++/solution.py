n = int(input())
y=0
for i in range(n):
    x=str(input())
    if (x[0]=="+"and x[1]=="+")or (x[2]=="+"and x[1]=="+"):
        y=y+1
    else:
        y=y-1
print(y)