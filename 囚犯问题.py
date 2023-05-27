# 执行枪决
def kill(__prisoners__):
    lst = []
    ok = False
    for __prisoner__ in __prisoners__:
        if ok:
            lst.append(__prisoner__)
        # 翻转ok
        if ok:
            ok = False
        else:
            ok = True
    return lst


# 准备囚徒名单
prisoners = []
for i in range(1, 101):
    prisoners.append(i)
print(prisoners)

# 循环执行枪决
while len(prisoners) > 1:
    prisoners = kill(prisoners)
    print(prisoners)
