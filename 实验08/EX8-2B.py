import pandas as pd

DF_check =pd.read_excel("info.xlsx","checkup",header=1,index_col=0,usecols=[0,2,4,5]) # 1.读取需要的数据，将本行代码补充完整

DF_check.eval('weight_kg=weight/2.204',inplace=True)  # 2.换算体重，将本行代码补充完整
DF_check["temp"]=((DF_check["temp"]-32)/1.8).round(1) # 3.换算体温，将本行代码补充完整
DF_check["country"].replace("EN","UK",inplace=True)  # 4.完成替换操作，将本行代码补充完整
DF_check.sort_values(["temp","weight"],ascending=[True,False],inplace=True)  # 5.完成排序操作，将本行代码补充完整

#DFout =DF_check[(DF_check["country"]=="US")|(DF_check["temp"]>37.3)]  # 6.筛选出需要的数据，将本行代码补充完整
DFout =DF_check.query("(country=='US') or (temp>37.3)")

DFout.to_excel("result.xlsx",sheet_name="test",startcol=2)   # 7.将DFout写入到excel文件，将本行代码补充完整

