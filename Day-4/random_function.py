#To use the random module we need to import the modules as shown below
import random

#To generate random integers for a range of numbers, we can do it by below method
random_int = random.randint(1,100)

#To generate random floating point numbers we use below mentioned way
#random.random() only returns the next random floating point number between [0.0 to 1.0)
random_float = random.random()

#To generate random floating point numbers beyond 1.0, we use below mentioned menthod
random_float_1 = 5*(random.random())

print(random_int)
print(random_float)
print(random_float_1)