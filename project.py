import os
import shutil

from_dir="C:/Users/Rehana/Downloads"
to_dir="C:/Users/Rehana/Desktop"

list_dir=os.listdir(from_dir)

for i in list_dir:
    name,ext=os.path.splitext(i)

    if ext=="":
        continue
    if ext in[".txt",".doc",".docx",".pdf"]:
        path1=from_dir+"/"+ i
        path2=to_dir+"/"+"PDF Files"
        path3=to_dir+"/"+"PDF Files"+"/"+i

        if os.path.exists(path2):
            print("Moving" + i)
            shutil.move(path1,path3)
    
        else:
            os.makedirs(path2)
            print("Moving" + i)
            shutil.move(path1,path3)