from domain import * 
import math
import os 
import pickle 
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
            with open("students.pickle","wb") as file:
                pickle.dump(str(self.stu_list) + "\n",file)
                
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
            with open("courses.pickle","wb") as file:
                pickle.dump(str(self.course_list) +"\n",file)
            
    def set_mark(self,stu_name,course_name):
        mark = float(input())
        mark = math.floor(mark*10)/10
        if mark > 25 or mark < 0 :
            print("Error mark input ! too high or too small")
            return 0 
        else:
            self.mark_dict[(stu_name,course_name)] = mark
            with open("marks.pickle","wb") as file:
                pickle.dump(str(self.mark_dict),file)
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
        

class Save:
    def compress():
        with open("students.dat","a") as outfile:
            with open("students.pickle","rb") as infile:
                data_1 = pickle.load(infile)
                outfile.write("Students:\n")
                for stu in eval(data_1):
                    outfile.write(f"student id = {stu[0]}, name = {stu[1]}, date of birth = {stu[2]}\n")
            with open("courses.pickle","rb") as infile:
                data_2 = pickle.load(infile)
                outfile.write("\nCourses:\n")
                for course in eval(data_2):
                    outfile.write(f"course id = {course[0]}, course name = {course[1]}, numbers of credits = {course[2]}\n")
            with open("marks.pickle","rb") as infile:
                data_3 = pickle.load(infile)
                outfile.write("\nMarks:\n")
                for mark in eval(data_3).items():
                    outfile.write(f"in the {mark[0][1]}, {mark[0][0]}: {mark[1]}\n")
        if os.path.exists("students.pickle"):
            os.remove("students.pickle")
        if os.path.exists("courses.pickle"):
            os.remove("courses.pickle")
        if os.path.exists("marks.pickle"):
            os.remove("marks.pickle")

class Open:
    def decompress():
        print("------------------------------------")
        if os.path.exists("students.dat"):
            with open("students.dat","r") as f:
                print(f.read())
        os.remove("students.dat")