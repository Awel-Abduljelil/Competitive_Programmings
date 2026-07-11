n = int(input())
l=[]
for i in range(n):
    x=input()
    if len(x)>10:
        y=len(x)-2
        
        print(x[0]+str(y)+x[-1])
    else:
        print(x)