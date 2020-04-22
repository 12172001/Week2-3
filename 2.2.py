n = int(input())
if 10 < n < 20:
    print(n, "korov")
elif n % 10 == 0 or (n % 10 >= 5 and n % 10 <= 9):
    print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
else:
    print(n, "korovy")
