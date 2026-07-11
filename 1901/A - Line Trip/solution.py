t = int( input())
for i in range(t):
     n , x = map(int , input().split())
     a = list(map(int, input().split()))
     a.insert(0 , 0)
     a.append(x)
     max_fuel = 0
     for i in range(n+1):
        if i== n:
            if max_fuel < 2*(a[i+1] - a[i]):
                max_fuel = 2*(a[i+1] - a[i])
        elif max_fuel < (a[i+1] -a[i]):
            max_fuel = a[i+1] -a[i]
     print(max_fuel)