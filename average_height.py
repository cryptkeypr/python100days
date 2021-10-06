# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆
total = 0
length = 0

for n in student_heights:
  total += n
  length += 1

avg = total // length
print(f"The average height of students is: {avg}.")
