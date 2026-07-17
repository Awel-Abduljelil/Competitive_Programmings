t = int(input())
for _ in range(t):
    k,q = map(int,input().split())
    a = list(map(int,input().split()))
    n = list(map(int,input().split()))
    min_a = min(a)
    output = []
    for i in range(q):
        if n[i] < min_a:
            output.append(n[i])
        else:
            output.append(min_a - 1)
    
    print(*output)