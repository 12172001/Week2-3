P = float(input())
X = float(input())
Y = float(input())
money1 = 100 * X + Y
money2 = int(money1 * (100 + P) / 100)
print(money2 // 100, money2 % 100)
