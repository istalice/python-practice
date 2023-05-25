mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numlist =[]

for num  in mylist:
    if num % 2 == 0:
      numlist.append(num)

print(f"输出数字为：{numlist}" , end='')