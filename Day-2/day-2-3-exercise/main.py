# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#type conversion of age 
age = int(age)

#years left until the age of 90
yearsLeft = 90 - age

#calculating days, weeks and months left until the age of 90
daysLeft = yearsLeft*365
weeksLeft = yearsLeft*52
monthsLeft = yearsLeft*12

#printing the values using f-strings
print(f'You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.')
