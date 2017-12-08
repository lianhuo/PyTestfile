print("=" * 50)
print(" 名字管理系统v1.1")
print(" 1：添加名字")
print(" 2：删除名字")
print(" 3：查询名字")
print(" 4：修改名字")
print(" 5：退出系统")

names = []

while True:
    num = int(input("请选择序号："))
    if num == 1:
        new_name = input("请输入添加的名字")
        names.append(new_name)
        print(names)
    elif num == 2:
        del_name = input("请输入删除的名字")
        if del_name in names:
            names.remove(del_name)
            print(names)
        else:
            print("没有这个人,无法删除")
    elif num == 3:
        find_name = input("请输入查询的名字")
        if find_name in names:
            print("找到了：%s" % find_name)
        else:
            print("没有这个人")
    elif num == 4:
        update_name = input("请输入要修改的名字")
        if update_name in names:
            newupdate_name = input("请输入修改后的名字")
            for name in names:
                if update_name == name:
                    #获取要修改的下标
                    pass
            print(names)
        else:
            print("没有这个人")
        pass
    elif num == 5:
        break
    else:
        print("请输入1~5序号")


