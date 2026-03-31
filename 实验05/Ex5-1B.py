def bmieng(w,h,n=2):
    c=(0.454*w)/((2.54*h*0.01)**2)
    c=round(c,n)
    return c

# Please complete the custom function code
A = bmieng(198, 66)
B = bmieng(121, 68.5)
print("Patient A BMI value: ",A)
print("Patient B BMI value: ",B)