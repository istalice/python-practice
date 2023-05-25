mylist = [21, 25, 21, 23, 22, 20]
  #定义这个列表，并用变量接受它
print(f"输出这个列表为：{mylist}")
  #追加了一个数字31，到列表尾部
mylist.append(31)
print(f"输出这个列表为：{mylist}")
  #追加一个新列表[29，33， 30]，到列表尾部
mylist.extend([29, 33, 30])
print(f"输出这个列表为：{mylist}")
  #取出第一个元素
x = mylist[0]
print(f"取出第一元素是：{x}")
  #取出最后一个元素
num2 = mylist[-1]
print(f"取出最后一个元素是：{num2}")
  #查找元素31，在列表中的下标位置
x = mylist.index(31)
print(f"下标位置是：{x}")

