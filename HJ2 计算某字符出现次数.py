s = input().lower()
c = input().lower()
count = 0
for i in range(len(s)):
    c1 = s[i]
    if c1 == c:
        count += 1
print(count)
