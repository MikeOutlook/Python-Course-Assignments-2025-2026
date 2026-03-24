def bmieng(w,h,n=2):
    c=(0.454*w)/((2.54*h*0.01)**2)
    c=round(c,n)
    return c

# 请同学们完成自定义函数代码
A = bmieng(198, 66)
B = bmieng(121, 68.5)
print("患者 A 的 BMI 值是： ",A)
print("患者 B 的 BMI 值是： ",B)