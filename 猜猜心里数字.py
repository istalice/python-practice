num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜第一次就猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("猜对了")
else:
    print("Sorry,全部猜错啦，我想的是：%d" % num)



