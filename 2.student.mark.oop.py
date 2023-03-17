import math
list_course_name = []
list_student_name = []


class Student:
    def __init__(self,sid = str(),name = str(),dob = str()):
        self.sid = sid 
        self.name = name
        self.dob = dob
    def get_sid(self):
        return self.sid
    @property
    def set_sid(self):
        self.sid = input("Please enter id of student: ")
    def get_name(self):
        return self.name
    @property
    def set_name(self):
        self.name = input("Please enter name of student: ")
        list_student_name.append(self.name)
    def get_dob(self):
        return self.dob 
    @property
    def set_dob(self):
        self.dob = input("Please enter date of birth: ")     

            
class All_students():
    def __init__(self,num_stu):
        self.num_stu = num_stu
        self.stu_list = []
    def add_student(self):
        for i in range(self.num_stu):
            single_stu = Student()
            single_stu.set_sid
            single_stu.set_name
            single_stu.set_dob
            self.stu_list.append(single_stu)
    def display_students_infor(self):
        print("---------------------------------------------")
        for students in self.stu_list:
            print("Student id :",students.get_sid())
            print("Student's name :",students.get_name())
            print("Date of birth :",students.get_dob())
        print("----------------------------------------------")
            
                        
class Courses:
    def __init__(self,cid = str(),c_name = str()):
        self.cid = cid
        self.c_name = c_name
    def get_cid(self):
        return self.cid 
    def set_cid(self):
        self.cid = input("Enter course id: ")
    def get_course_name(self):
        return self.c_name
    def set_course_name(self):
        self.c_name = input("Enter course name:")
        list_course_name.append(self.c_name)

            
class All_Courses:
    def __init__(self,num_c):
        self.num_c = num_c
        self.course_list = []
    def add_course(self):
        for i in range(self.num_c):
            single_course = Courses()
            single_course.set_cid()
            single_course.set_course_name()
            self.course_list.append(single_course)
    def display_courses(self):
        print("---------------------------------------------")
        for courses in self.course_list:
            print("course id :" ,courses.get_cid())
            print("course name :",courses.get_course_name())
        print("---------------------------------------------")
            
    
class Marks():
    def __init__(self,mark = None):
        self.mark = mark 
        self.marks_dict = {}
    def get_mark(self,stu_name,course_name):
        return self.marks_dict.get((stu_name, course_name), None)
    def set_mark(self,stu_name,course_name):
        mark = float(input())
        mark = math.floor(mark*10)/10
        if mark > 25 or mark < 0 :
            print("Error mark input ! too high or too small")
            return 0 
        else:
            self.marks_dict[(stu_name,course_name)] = mark
        
        
        
class All_Mark(All_students,All_Courses):
    def __init__(self, num_stu, num_c):
        super().__init__(num_stu)
        All_Courses.__init__(self, num_c)
        self.marks = Marks()
    def add_marks(self):
        self.course_name = input("Enter the course that you want to mark for the student :")
        if self.course_name not in list_course_name:
            print("The course that you entered not in the list !")
        else: 
            print(f"for the {self.course_name} course:")
            for self.stu_name in list_student_name:
               print(f"Enter the mark for {self.stu_name}",end = " ")
               self.marks.set_mark(self.stu_name,self.course_name)
            print("-------------------------------------------------")
            
    def display_marks(self):
        print("------------------------------------------------")
        course_name = input("Enter the course name that you want to display marks: ")
        if course_name not in list_course_name:
            print("No courses was found !")
            return 0
        else:
            print(f"Marks for {course_name}")
            for self.stu_name in list_student_name:
                mark = self.marks.get_mark(self.stu_name,course_name)
                print(f"{self.stu_name} : {mark}")
            print("------------------------------------------------")

def main():                
    num_stu = int(input("Enter number of students:"))
    all_students = All_students(num_stu)
    all_students.add_student()
    num_c = int(input("Enter number of courses: "))
    all_courses = All_Courses(num_c)
    all_courses.add_course() 
    all_mark = All_Mark(num_stu,num_c)
          
    while True:
        options = {"option 1":"list students",
                "option 2":"list courses",
                "option 3":"Input mark",
                "option 4":"display mark",
                "option 5":"Break"}
        for key,value in options.items():
            print(key,":",value)
        choice = input("choose 1 , 2 , 3 , 4 , 5 :")
        if choice == "1":
            all_students.display_students_infor()          
        elif choice == "2":
            all_courses.display_courses()
        elif choice == "3":
            all_mark.add_marks()
        elif choice == "4":
            all_mark.display_marks()
        elif choice == "5":
            break  
if __name__ == "__main__":
    main() 