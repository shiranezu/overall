class DuplicateStudentIDError(Exception):
    pass
class StudentNotFoundError(Exception):
    pass

class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        

class student_record_manager:
    def  _init_(self, file_path="records.txt"):
        self.file_path = file_path

    def add_student(self, student : Student) -> None:
        students = self._read_records()
        if student.id in students:
            raise DuplicateStudentIDError('ID already exists.')
        students[student.id] = student 
        self.write_records(students)

    def get_student(self, id: int) -> Student:
        students = self.read_records()
        if id not in students:
            raise StudentNotFoundError('Stusent id not found.')
        return students[id]


    def update_student(self, student: Student) -> None:
        students = self._read_records()
        if student.id not in students:
            raise StudentNotFoundError('ID not found.')
        students[student.id] = student
        self.write_records(students)
   
    def _read_records(self):
        students = {}
        with open(self.file_path, "r") as file:
            for line in file:
                student_id, name, age = line.strip().split(",")
                student_id = int(student_id)
                age = int(age)
                students[student_id] = Student(student_id, name, age)
        return students

    def _write_records(self, students):
        with open(self.file_path, "w") as file:
            for student_id, student in students.items():
                file.write(f"{student_id},{student.name},{student.age}\n")