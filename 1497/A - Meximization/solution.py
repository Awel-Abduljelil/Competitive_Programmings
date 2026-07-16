t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    lst = []
    b = set()
    for i in range(n):
        if a[i]  in b:
            lst.append(a[i])
        else:
            b.add(a[i])
    if lst :
        output = sorted(list(b)) + sorted(lst)
    else:
        output = sorted(list(b)) 
    print(*output)