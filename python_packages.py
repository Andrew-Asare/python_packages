# from random import random # generates random numbers
import math
# print(random())
#
# num_float = 23.4
# print(round(num_float))
# print(math.ceil(num_float)) # math.ceil will always round up
# print(math.floor(num_float)) # Opposite of math.ceil
# print("actual float value" + str(num_float))

import os
import datetime, sys
working_directory = os.getcwd() # it tells us the current dir location
# print(working_directory)
# print(os.uname()) # works on Linux
print(os.cpu_count())
print(datetime.date.today())
print(sys.path)
print(math.pi)