import re

txt='@mipmop/icon_home_18111'

re1='(@)'	# Any Single Character 1
re2='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
re3='(\\/)'	# Any Single Character 2
re4='((?:[a-z][a-z0-9_]*))'	# Variable Name 2

nd=re1+re2+re3+re4
print nd
rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    c1=m.group(1)
    var1=m.group(2)
    c2=m.group(3)
    var2=m.group(4)
    print "("+c1+")"+"("+var1+")"+"("+c2+")"+"("+var2+")"+"\n"