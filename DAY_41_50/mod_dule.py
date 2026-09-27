#importing modules and how to use it
#normal importation 
'''import math
print(math.sqrt(9)) '''
#for specific function, no need to mention
'''from math import sqrt,pi
print(sqrt(4))
print(pi)''' 
#want to import everything 
'''from math import * # not prefereable cuz if more than one module have same function name then
#it might cause confusion
print(sqrt(9)) '''
#renaming the module function
'''from math import sqrt as s 
print(s(16))'''
#renaming the module
'''import math as i_hate_math
print(i_hate_math.sqrt(9))
print(dir(i_hate_math))
print(i_hate_math.nan,type(i_hate_math.nan))'''




