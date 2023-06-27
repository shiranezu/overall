#  Write a function called calculate_grades that takes a list of student grades as input and returns a dictionary that contains the number of students who received each grade. Grades are given as integers ranging from 0 to 100, and are divided into five categories: "A" for grades 90-100, "B" for grades 80-89, "C" for grades 70-79, "D" for grades 60-69, and "F" for grades below 60. Your function should use a loop and an if statement to count the number of students who received each grade.
# Here's an example input and output to help clarify what your function should do:
# grades = [80, 95, 70, 65, 88, 92, 75, 60, 85, 78, 92, 63, 55]
# print(calculate_grades(grades)) 
# Output: {'A': 3, 'B': 3, 'C': 3, 'D': 3, 'F': 3}
# Explanation: In the input list [80, 95, 70, 65, 88, 92, 75, 60, 85, 78, 92, 63, 55], there are three students who received grades between 90-100 (A), three students who received grades between 80-89 (B), three students who received grades between 70-79 (C), three students who received grades between 60-69 (D), and three students who received grades below 60 (F). Therefore, the output of the calculate_grades function is {'A': 3, 'B': 3, 'C': 3, 'D': 3, 'F': 3}.

def calculate_grades(grades):
    grade_range= {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for i in grades:
        if grade_range>= 90:
            print ['A']
        elif grade_range>=80:
            print ['B']
        elif grade_range>=70:
            print ['C']
        elif grade_range>=60:
            print ['D']
        else:
            print ['F']
    
    return grade_range
calculate_grades= ([70, 80, 60, 75])