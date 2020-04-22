n = int(input())
ans = 0
while n != 0:
    if n % 2 == 0:
        ans += 1
    n = int(input())
print(ans)
