import os


unlock_str="encrypt"
for each_file in os.listdir("."):
	if each_file.endswith(".md"):
		lines=[]
		cnt=0
		with open(each_file,"r",encoding="utf-8") as f:
			lines=f.readlines()
		new_lines=[each for each in lines if not unlock_str in each]
		new_lines_str="".join(new_lines)
		with open(each_file,"w",encoding="utf-8") as f:
			f.write(new_lines_str)
print("done.")