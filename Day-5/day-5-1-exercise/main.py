# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_heights = 0
length = 0

for height in student_heights:
  sum_heights += height
  length +=1

avg_height = round(sum_heights/length)

print(avg_height)

  