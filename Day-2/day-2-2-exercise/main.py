# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#type conversion of input values
weight=float(weight)
height=float(height)

#BMI Calculation formula
BMI = weight/(height**2)

#type casting and printing the calculated BMI Value 
print("Your BMI is: ", int(BMI))










