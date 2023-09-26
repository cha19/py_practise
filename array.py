import array
import random

valuelist=array.array('i',100)

for i in range(len(valuelist)):
    valuelist[i]=random.random()

for value in valuelist:
    print(value)

'''
    from array import Array
import random
valuelist=Array(100)
for i in range(len(valuelist)):
    valuelist[i]=random.random()

for value in valuelist:
    print(value)

'''