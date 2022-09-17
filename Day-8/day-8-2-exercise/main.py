import math
import time
#Write your code below this line 👇
def prime_checker(number):
  flag = True
  num_sqrt = round(math.sqrt(number))
  for i in range(2,num_sqrt+1):
    if number%i == 0:
      print("Given Number is not Prime")
      flag = False
      break
    else:
      flag = True

  if flag == True:
    print("Given Number is Prime")

#Write your code above this line 👆
t0 = time.time()
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
t1 = time.time()

print("Time Taken: ", t1-t0)




