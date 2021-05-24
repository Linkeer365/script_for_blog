import os

for each in os.listdir("."):
	if each.endswith(".md"):
		old_list=[]
		with open(each,"r",encoding="utf-8") as f:
			old_list=f.readlines()
		flag=0
		for eachidx,eachLine in enumerate(old_list):
			if "tags" in eachLine:
				flag+=1
			if "- " in eachLine:
				flag+=1
			if flag==2:
				del old_list[eachidx]
				flag=0
		new_str="".join(old_list)
		with open(each,"w",encoding="utf-8") as f:
			f.write(new_str)
print("done.")