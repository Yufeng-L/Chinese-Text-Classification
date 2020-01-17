#Cut the idnum
#字符串分割 6/8/4
import os,sys

#排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码:


files = os.listdir("C:/Users/yflin/Desktop/id2")

for filename in files:
	path = "C:/Users/yflin/Desktop/id2/" + filename 
	with open(path,"r") as f:
		s = f.read()
		f.close()
	with open(path,"w") as f:
		new_s = ""
		for i in range(0,6):
			new_s += s[i]
		new_s += " "
		for i in range(6,14):
			new_s += s[i]
		new_s += " "
		for i in range(14,18):
			new_s += s[i]

		f.write(new_s)
		f.close()

