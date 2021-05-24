import os

md_files=[]
for each in os.listdir("."):
	if each.endswith(".md"):
		md_files.append(each)

lock_str="encrypt: true\n"
for each in md_files:
	lines=[]
	with open(each,"r",encoding="utf-8") as f:
		lines=f.readlines()
	cnt=0
	idx=0
	for each_idx,each_val in enumerate(lines):
		if "---" in each_val:
			cnt+=1
		if cnt==2:
			idx=each_idx
			break
	lines.insert(idx,lock_str)
	lines_str="".join(lines)
	with open(each,"w",encoding="utf-8") as f:
		f.write(lines_str)
print("done.")