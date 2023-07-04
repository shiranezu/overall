import random 
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def get_grades(self):
        if self.score < 30:
            return 'F'
        elif self.score < 40:
            return 'E'
        elif self.score < 60:
            return 'D'
        elif self.score < 70:
            return 'B'
        else:
            return 'A'

names = ['Urban', 'Soap', 'Nickolai', 'Yuri\n', 'Frost', 'Ghost', 'Gaz', 'Park', 'Mark', 'Jack', 'John']

with open('names.txt', 'w') as f:
    for name in names:
        f.write(f"{name} \n")

with open('names.txt', 'r') as f:
    read_lines = f.readlines()

students = []
for name in names:
        age = random.randint(16, 19)
        score = random.randint(20, 100)
        student = Student(name, age, score)
        students.append(student)

for student in students:
    print(f"Name: {student.name}, Age: {student.age}, Score: {student.score,}, Grade : {student.get_grades()}")
    
  
   


    