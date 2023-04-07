class Student():
    def __init__(self,sid = str(),name = str(),dob = str()):
        self.sid = sid 
        self.name = name 
        self.dob = dob
        self.stu_list = []
class Course():
    def __init__(self,cid = str(),c_name =  str(), credits = int()):
        self.cid = cid 
        self.c_name = c_name
        self.credits = credits 
        self.course_list = []
class Mark():
    def __init__(self,mark = None):
        self.mark = mark 
        self.mark_dict = {}