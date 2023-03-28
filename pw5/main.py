from output import *

                        
def main():    
    output_data = Output()
    output_data.add_student()
    output_data.add_course()  
    while True:
        options = {"option 1":"list students",
                "option 2":"list courses",
                "option 3":"Input mark",
                "option 4":"display mark",
                "option 5":"display gpa",
                "option 6":"Sort students gpa",
                "option 7":"compress",
                "option 8":"decompress",
                "option 9":"Break"}
        for key,value in options.items():
            print(key,":",value)
        choice = input("choose 1 , 2 , 3 , 4 , 5 ,6 ,7: ")
        if choice == "1":
            output_data.display_students_info()          
        elif choice == "2":
            output_data.display_courses_info()
        elif choice == "3":
            output_data.add_marks()
        elif choice == "4":
            output_data.display_marks()
        elif choice == "5":
            output_data.calculate_gpa()
        elif choice == "6":
            output_data.sort_students_by_gpa()
        elif choice == "7":
            Save.compress()
        elif choice == "8":
            Open.decompress() 
        elif choice == "9":
            break
if __name__ == "__main__":
    main()