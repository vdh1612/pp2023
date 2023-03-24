from domain import * 
import math


class Input(Student,Course,Mark):
    list_course_name = []
    list_student_name = []
    list_credits = []
    def __init__(self,sid = str(),name = str(),dob = str(),cid = str(),c_name = str(), credits = int(),mark = None):
        Student.__init__(self,sid,name,dob)
        Course.__init__(self,cid,c_name,credits)
        Mark.__init__(self,mark)
    def set_sid(self):
        self.sid = input("Please enter your student id:")
        return self.sid
    def set_name(self):
        self.name = input("Please enter your student name:")
        Input.list_student_name.append(self.name)
        return self.name
    def set_dob(self):
        self.dob = input("Please enter your date of birth:")
        return self.dob
    def add_student(self):
        self.num_student = int(input("Enter number of students :"))
        for i in range(self.num_student):
            sid = self.set_sid()
            name = self.set_name()
            dob = self.set_dob()
            self.stu_list.append((sid,name,dob))
    def set_cid(self):
        self.cid = input("Please enter your course Id:")
        return self.cid
    def set_course_name(self):
        self.c_name = input("Enter course name:")
        Input.list_course_name.append(self.c_name)
        return self.c_name
    def set_credits(self):
        self.credits = int(input("Enter credits for this course:"))
        Input.list_credits.append(self.credits) 
        return self.credits
    def add_course(self):
        self.num_c = int(input("Enter number of courses: "))
        for i in range(self.num_c):
            cid = self.set_cid()
            course_name = self.set_course_name()
            credits = self.set_credits()
            self.course_list.append((cid,course_name,credits))
    def set_mark(self,stu_name,course_name):
        mark = float(input())
        mark = math.floor(mark*10)/10
        if mark > 25 or mark < 0 :
            print("Error mark input ! too high or too small")
            return 0 
        else:
            self.mark_dict[(stu_name,course_name)] = mark
    def add_marks(self):
        self.course_name = input("Enter the course name that you want to add marks:")
        if self.course_name not in Input.list_course_name:
            print("The course id not exist !")
            return 0
        else:
            print(f"for the course {self.course_name} :")
            for self.stu_name in Input.list_student_name:
                print(f"Enter the mark for {self.stu_name}:",end = " ")
                self.set_mark(self.stu_name,self.course_name)
            print("------------------------------------")    
        