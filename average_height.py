student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
number_of_students = len(student_heights)
total_height = sum(student_heights)
average_height = round(total_height / number_of_students)
print(f"total height {total_height}\nnumber of students = {number_of_students}\naverage height = {average_height}\n ")
