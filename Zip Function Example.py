
zipped_list = list(zip( ['A' , 'B', 'C', 'D', 'E'], [67,34,78,85,65]))

print(zipped_list)

student_names, student_marks = zip(*zipped_list)

print(list(student_names), list(student_marks))