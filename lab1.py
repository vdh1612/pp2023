def number_student():
    return  int(input("Enter amount of students in class :"))
def get_infor():
    sid = input("Enter student id: ")
    name = input("Enter name of the student:")
    dob = input("Enter date of birth:")
    return sid,name,dob
def list_students():
    for i in range(len(sid_lst)):
        print("The student id:",sid_lst[i])
        print("Name: ",name_students[i])
        print("Date of birth:",dob_lst[i])
def get_num_course():
    return int(input("Enter number of courses: "))
def get_course_infor():
    print("Enter course id :",end =" ")
    cid = input()
    name_course = input("Enter name of the course:")
    return cid,name_course    
def list_course():
    for i in range(0,len(cid_lst)):
        print("Course id:"+cid_lst[i])
        print("Name of the course:"+course_name_lst[i])
mark_lst = []
course_name_choice = []
def input_mark():
    cid = input("Enter the id of the course that you want to mark:")
    if cid not in cid_lst:
        print("No course was found!")   
        return 0
    print("Enter the name of the course has id",cid,":",end = " ")
    course_name = input()
    if course_name not in course_name_lst:
        print("Error name of the course !")
        return 0
    course_name_choice.append(course_name)    
    for name in name_students:
        print("please enter the mark for",name,":",end = " ")
        mark = int(input())
        mark_lst.append(mark)
def display_mark():
    print("In the",course_name_choice[0],"course:",end = "\n")
    for i in range(0,len(name_students)):
        print("{0}'s mark is:{1}".format(name_students[i],mark_lst[i]))
num_student = number_student()
sid_lst = []
name_students = []
dob_lst = []
for i in range(num_student):
    sid,name,dob = get_infor()
    sid_lst.append(sid)
    name_students.append(name)
    dob_lst.append(dob)
num_course = get_num_course()
cid_lst = []
course_name_lst = []
for i in range(num_course):
    cid,name_course = get_course_infor()
    cid_lst.append(cid)
    course_name_lst.append(name_course)
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
        list_students()
    elif choice == "2":
        list_course()
    elif choice == "3":
        input_mark()
    elif choice == "4":
        display_mark()
    elif choice == "5":
        break 