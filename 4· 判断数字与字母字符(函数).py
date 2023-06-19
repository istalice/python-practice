def if_str(x):
    if 0 <= x <= 9 or 'a' <= x <= 'z' or 'A' <= x <= 'Z':
        return "ture"
    else:
        return "false"

x = input("请输入：")
print(if_str(x))

