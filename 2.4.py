n = int(input())
mx = n
ans = 1
while n != 0:
    n = int(input())
    if n == mx:
        ans += 1
    elif n > mx:
        mx = n
        ans = 1
print(ans)
