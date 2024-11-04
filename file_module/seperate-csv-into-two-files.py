file = open('students_points.csv', 'r')
string = file.read()

names_file = open('student_names.txt', 'a')
points_file = open('student_points.txt', 'a')

for student in string.split('\n')[1:len(string.split('\n'))-1]:
  names_file.write(student.split(',')[0] + '\n')
  points_file.write(student.split(',')[1] + '\n')