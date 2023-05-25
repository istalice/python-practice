#这是程序生成随机数字
import random
num = random.randint(1, 100)
guess_n = int(input("请输入你的数字："))
# 通过if语句来判断
if guess_n ==  num:
    print("恭喜第一次就猜对了！")
#没猜对 就有三次机会 再else 里面做
else:
    if guess_n >num:
        print("你猜大了")
    else:
        print("你猜小了")
#以上代码就是一次机会
    guess_n = int(input("再猜一次，请输入你的数字："))
    if guess_n == num:
        print("恭喜你猜对了")
    else:
        if guess_n > num:
           print ("你猜大了")
        else:
           print ("你猜小了")

        guess_n = int(input("最后再猜一次，请输入你的数字："))
        if guess_n == num:
            print("恭喜你 猜对了")
        else:
            print("机会用完了，没有猜中")






