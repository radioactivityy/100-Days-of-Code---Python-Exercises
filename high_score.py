student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
final = max(student_scores)
print(f"The highest score in the class is: {final}")