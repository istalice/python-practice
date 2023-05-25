#程序猜数字
import random
num = random.randint(1, 100)
#记录猜了几次
count = 0
flat = True
while flat:
    guess_n = int(input("请输入猜想数字："))
    count += 1
    if guess_n == num:
       print("恭喜你猜对了")
       #设置False 是终止循环条件
       flat = False
    else:
        if guess_n > num:
            print("猜大了")
        else:
            print("猜小了")

print(f"你一共猜了{count}次")