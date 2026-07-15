t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    lst = set([])
    count = 0
    for i in range(n):
        if s[i] in lst:
            count += 1
        else:
            lst.add(s[i])
            count += 2
    print(count)