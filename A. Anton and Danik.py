n = int(input())
s = input().strip()
antonwin = s.count('A')
danikwin = s.count('D') 
if antonwin > danikwin:
    print("Anton")
elif danikwin > antonwin:
    print("Danik")
else:
    print("Friendship")
