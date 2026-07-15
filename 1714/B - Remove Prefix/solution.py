t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    lst.reverse()
    seen = set()
    move = 0
    for i in range(n):
        if lst[i] in seen:
            break
        seen.add(lst[i])
        move +=1
           
    print(n-move)
        