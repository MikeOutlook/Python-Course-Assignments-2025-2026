starlist=["一星","二星","三星"]
score=int(input("请输入员工评分："))
star=score//10
level=starlist[star]
print("该员工得分为{0}，等级为{1}".format(score,level))