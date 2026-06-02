n, h = map(int, input().split())
a = list(map(int, input().split()))
road_width = 0
for height in a:
    if height > h:
        road_width += 2
    else:
        road_width += 1
print(road_width)
