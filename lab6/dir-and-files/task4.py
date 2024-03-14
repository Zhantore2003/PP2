import os
f = open(r"C:\KBTU\DONER\PP2\lab6\dir-and-files\sumtext.txt")
cnt = 0
for lines in f:
    cnt += 1
print("files has {} lines".format(cnt))