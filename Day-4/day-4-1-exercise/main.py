#Remember to use the random module
import random
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
random_int=random.randint(0,1)

if(random_int == 1):
    print("Heads")

elif(random_int == 0):
    print("Tails")