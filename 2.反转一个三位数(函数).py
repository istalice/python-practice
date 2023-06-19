def reveral(x):
    a = x % 100 % 10
    b = x % 100 // 10
    c = x // 100
    return a, b, c
y = int(input("请输入："))
print(reveral(y))
