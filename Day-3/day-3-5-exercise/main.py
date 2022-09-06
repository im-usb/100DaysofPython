# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_concat=name1.lower()+name2.lower()
#print(names_concat)

true_count = str(names_concat.count('t')+names_concat.count('r')+names_concat.count('u')+names_concat.count('e'))

love_count = str(names_concat.count('l')+names_concat.count('o')+names_concat.count('v')+names_concat.count('e'))

love_score = int(true_count+love_count)

#print(true_count)
#print(love_count)
#print(love_score)

if(love_score<10 or love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif(love_score>40 and love_score<50):
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")
