n = int(input())
lst = []
for i in range(n):
    a = int(input())
    if a not in lst:
        lst.append(a)
lst.sort()
for item in lst:
    print(item)
