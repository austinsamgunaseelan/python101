from  datetime import time , date , datetime
# import datetime

# import math 
# from math import prod , min , max , ceil , floor , sqrt , pi

sam = datetime.now()
print(sam.year)
print(sam.month)
print(sam.date)
print(sam.hour)
print(sam.minute)
print(sam.second)

austin = sam.strftime("%m-%d-%Y %H:%M:%S")
print(austin)