t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    middle = (a[0]+a[-1])//2
    right_move = a[-1] - middle
    left_move = middle - a[0]
    print(max(right_move, left_move))