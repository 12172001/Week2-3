n = int(input())
cnt = 1
ans = 1
now = n
while n != 0:
    n = int(input())
    if n != now:
        cnt = 1
        now = n
    else:
        cnt += 1
        ans = max(ans, cnt)
print(ans)
