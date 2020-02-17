# coding: GBK 
# 8-16 练习
# import module_name
import persomal_profile
persomal_profile.persomal_profile('yulong', 'zhu')
# import module_name as mn
import persomal_profile as pp
pp.persomal_profile('yulong', 'zhu')
# from module_name import function_name
from persomal_profile import persomal_profile
persomal_profile('yulong', 'zhu')
# from module_name import function_name as fn
from persomal_profile import persomal_profile as pp
pp('yulong', 'zhu')
# from module_name import *
from persomal_profile import *
persomal_profile('yulong', 'zhu')
