name = "张三"
print("你好{},今天是星期四".format(name))
weekday = "星期四"
print("你好{},今天是{}".format(name,weekday))
print("{1}有两株树， 一株是{0}， 还有一株也是{0}".format("枣树", "墙外"))
x = 761.34725
print("保留 2 位小数{:.2f}".format(x))
print("不保留小数位{:.0f}".format(x))
y = 123456789
print("逗号分隔整数{:,}".format(y))
print("指数形式表示{:.2e}".format(y))