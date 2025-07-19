from student import student  # Error: Module names can't start with numbers
import pickle
stud = [student(1,'Mahesh','CSE'),
        student(2,'Suresh','ECE'),
        student(3,'Ramesh','MECH')]

with open('student.data', 'wb') as f:
    for s in stud:
        pickle.dump(s, f)