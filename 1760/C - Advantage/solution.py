t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    lst = sorted(a)
    strangest = lst[-1]
    second_strangth = lst[-2]
    output = []
    for i in range(n):
        if a[i]  == strangest:
            output.append(a[i] - second_strangth)
        else:
            output.append(a[i] - strangest)
    
    print(*output)