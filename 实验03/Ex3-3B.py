hb=int(input("请输入血红蛋白值："))
if hb >165:
    print("血红蛋白增多")
elif hb >120:
    print("血红蛋白正常")
elif hb >91:
    print("轻度贫血")
elif hb >61:
    print("中度贫血")
elif hb >30:
    print("重度贫血")
else:
    print("极度贫血")
