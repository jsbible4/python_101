# import myfunc

# 모듈 자체 가져오기
# myfunc.add()   # python file 하나하나는 다 module 이다.

# 모듈 안에 일부 함수만 가져오기
import myfunc
from myfunc import minus
print(myfunc.minus(4,1))
# from functools import reduce
# import functools
# functools.reduce()
#
# # 별칭으로 모듈 가져오기
# import myfunc as mf
# mf.minus()
#
# import math
# math.pi
#
# from datetime import  date
# today = date.today()
# print(today)

import os
home_path = os.path.expanduser('~')
desktop_path = os.path.join(home_path, 'Desktop')
folder_name = 'megastudy 최고'
new_folder_path = os.path.join(desktop_path,folder_name)
os.makedirs(new_folder_path,exist_ok=True)
# 자체적으로 컴퓨터에 폴더가 생성되게 함.

