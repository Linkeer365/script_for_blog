import os

for each in os.listdir("."):
	if each.endswith(".md"):
		old_list=[]
		with open(each,"r",encoding="utf-8") as f:
			old_list=f.readlines()
		for eachidx,eachLine in enumerate(old_list):
			if "- " in eachLine:
				del old_list[eachidx]
		new_str="".join(old_list)
		with open(each,"w",encoding="utf-8") as f:
			f.write(new_str)
print("done.")