def number_student():
    return  int(input("Enter amount of students in class :"))
def get_infor():
    sid = input("Enter student id: ")
    name = input("Enter name of the student:")
    dob = input("Enter date of birth:")
    return sid,name,dob
def list_students(student_list):
   for v in student_list:
       print(v)
def get_num_course():
    return int(input("Enter number of courses: "))
def get_course_infor():
    print("Enter course id :",end =" ")
    cid = input()
    name_course = input("Enter name of the course:")
    return cid,name_course    
def list_course(course_list):
    for v in course_list:
        print(v)
mark_lst = []
def input_mark():
    cid = input("Enter the id of the course that you want to mark:")
    if cid not in course_lst:
        print("No course was found!")   
        return 0
    for name in name_students:
        print("please enter the mark for",name,":",end = " ")
        mark = int(input())
        mark_lst.append(mark)
    if sid not in student_lst:
        print("The student does not exist!")           
def display_mark():
    for i in range(0,len(name_students)):
        print("{0}'s mark is:{1}".format(name_students[i],mark_lst[i]))
num_student = number_student()
student_lst = []
name_students = []
for i in range(num_student):
    sid,name,dob = get_infor()
    student_lst.append(sid)
    student_lst.append(name) 
    name_students.append(name)
num_course = get_num_course()
course_lst = []
for i in range(num_course):
    cid,name_course = get_course_infor()
    course_lst.append(cid)
    course_lst.append(name_course)
while True:    
    options = {"1.":"list students",
            "2.":"list courses",
            "3.":"Input mark",
            "4.":"display mark",
            "5.":"Break"}
    for key,value in options.items():
        print(key,":",value)
    choice = input("choose 1 , 2 , 3 , 4 , 5 :")
    if choice == "1":
        list_students(student_lst)
    elif choice == "2":
        list_course(course_lst)
    elif choice == "3":
        input_mark()
    elif choice == "4":
        display_mark()
    elif choice == "5":
        break 
