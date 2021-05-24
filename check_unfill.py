import os
import shutil

if not os.path.exists("unfill"):
    os.mkdir("unfill")


for each in os.listdir("."):
    if each.endswith(".md"):
        with open("./{}".format(each),"r",encoding="utf-8") as f:
            lines=f.readlines()
        pic_num=0
        line_num=0
        for each_line in lines:
            if each_line.startswith("{% asset_img"):
                pic_num+=1
            elif each_line!="\n":
                line_num+=1
        line_num-=5

        if line_num>=pic_num:
            pass
        else:
            shutil.copy("./{}".format(each),"./{}".format("unfill"))

print("done.")