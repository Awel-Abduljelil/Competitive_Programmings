s = input()
sl =[]
c=0
for i in range(len(s)):
    if s[i] in sl:
        continue
    else:
        sl.append(s[i])
        c +=1
if c%2 ==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
