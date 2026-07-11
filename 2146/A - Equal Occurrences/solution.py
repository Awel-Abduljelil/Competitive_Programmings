t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
 
    freqs = list(freq.values())
    max_f = max(freqs)
 
    best = 0
 
    for k in range(1, max_f + 1):
        cnt = 0
        for f in freqs:
            if f >= k:
                cnt += 1
        best = max(best, k * cnt)
 
    print(best)