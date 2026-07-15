n = int(input())
s = list(input())
lst = ["0"]*10
 
 
for i in range(n):
    if s[i] == 'L':
        left_index = lst.index("0")
        lst[left_index ] = "1"
    elif s[i] == 'R':
        right_index = 9-lst[::-1].index("0")
        lst[right_index ] = "1"
    else:
        x_index =int(s[i])
        lst[x_index] = "0"
        
        
print("".join(lst))