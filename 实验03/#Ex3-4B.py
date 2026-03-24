# 摄氏温度数据
cel = [37.1, 36.8, 37.0, 37.4, 36.5]

# 转换并显示华氏温度
for celsius in cel:
    fahrenheit = (celsius * 9/5) + 32
    print(f"摄氏温度 {celsius}°C 转换为华氏温度 {fahrenheit:.1f}°F")

##如果不用f有没有更简单的写法？