# -*- coding: utf-8 -*-
hight = 1.75
mass = 80.5
bmi = mass / pow(hight, 2)
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')
pass
