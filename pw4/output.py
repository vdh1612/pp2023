import numpy as np 
import math 
from input import *
class Output(Input):
    def __init__(self,sid = str(),name = str(),dob = str(),cid = str(),c_name = str(), credits = int(),mark = None):
        Input.__init__(self,sid,name,dob,cid,c_name, credits,mark)
        self.list_gpa = []
    def display_students_info(self):
        for student in self.stu_list:
            print("Student id :",student[0])
            print("Student's name :",student[1])
            print("Date of birth :",student[2])
        print("----------------------------------------------")
    def display_courses_info(self):
        for course in self.course_list:
            print("course id :" ,course[0])
            print("course name :",course[1])
            print("This course has numbers of credits :",course[2])
            print("---------------------------------------------")
    def get_mark(self,stu_name,course_name):
        return self.mark_dict.get((stu_name,course_name),None)
    def display_marks(self):
        course_name = input("Enter the course name that you want to display marks: ")
        if course_name not in self.list_course_name:
            print("No courses was found !")
            return 0
        else:
            print(f"Marks for {course_name}")
            for self.stu_name in self.list_student_name:
                mark = self.get_mark(self.stu_name,course_name)
                print(f"{self.stu_name} : {mark}")
            print("------------------------------------------------")
    def calculate_gpa(self):
        print("------------------------------------------------")
        credits_array = np.array([self.list_credits])
        for self.stu_name in self.list_student_name:
            product_array = np.array([])
            for i in range(len(self.list_course_name)):
                course_name = self.list_course_name[i]
                mark = self.get_mark(self.stu_name,course_name)
                if mark is None:
                    print(f"No mark found for {self.stu_name}")
                    continue                
                product = mark * self.list_credits[i]
                product_array = np.append(product_array, product)
            total_credits = np.sum(credits_array)
            if len(product_array) > 0:
                gpa = round(np.sum(product_array) / total_credits,2)
                self.list_gpa.append(gpa)
                print(f"Gpa for {self.stu_name} : {gpa}")
        print("----------------------------------------------")
    def sort_students_by_gpa(self):
        self.calculate_gpa()
        print("----------------------------------------------")
        gpa_dict = dict(zip(self.list_student_name, self.list_gpa))
        sorted_gpa_dict = dict(sorted(gpa_dict.items(), key = lambda gpa: gpa[1], reverse=True))   
        print("After students's name are sorted by GPA (descending):")
        for student, gpa in sorted_gpa_dict.items():
            print(f"GPA of {student} : {gpa}")
        print("----------------------------------------------")
    