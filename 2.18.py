n = int(input())
mx2 = 0
mx1 = n
ans = 1
while n != 0:
    n = int(input())
    if n > mx1:
        mx2 = mx1
        mx1 = n
    else:
        if n > mx2:
            mx2 = n
print(mx2)
