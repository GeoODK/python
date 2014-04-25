import os
for i in os.walk('/home'):
    for j in i[2]:
        if j.endswith('.avi'):
            base = os.path.abspath(i[0])
            print "%s\%s"%(base, j)

            
raw_input('enter retrun to exit')
