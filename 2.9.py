a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if d > e:
    d, e = e, d
if d > f:
    d, f = f, d
if e > f:
    e, f = f, e
if a == d and b == e and c == f:
    print("Boxes are equal")
elif a <= d and b <= e and c <= f:
    print("The first box is smaller than the second one")
elif a >= d and b >= e and c >= f:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
