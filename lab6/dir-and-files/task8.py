import os
p=(r"C:\KBTU\DONER\PP2\lab6\dir-and-files\delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")