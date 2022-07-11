# coding:utf8

import datetime
import time
import timeit

# datetime format
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

# calculate elapsed time
start = timeit.default_timer()
time.sleep(2)
end = timeit.default_timer()
print(f"{end - start} seconds elapsed.")
