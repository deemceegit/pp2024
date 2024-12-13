def studentInfo():
    id = input("Enter ID:")
    name = input("Enter name:")
    dob = input("Enter DOB: ")
    return {"id" : id, "name" : name, "dob" : dob}

def courseInfo():
    id = input("Course ID: ")
    name = input("Course name: ")
    return {"id" : id, "name" : name}

def StudentNo():
    num = int(input("Enter number of students: "))
    student = []
    for i in range(num):
        temp = studentInfo()
        student.append(temp)
    return student

def CourseNo():
    num = int(input("Enter number of courses: "))
    course = []
    for i in range(num):
        temp = courseInfo()
        course.append(temp)
    return course

def listCourses(courses):
    print("\nCourse List:")
    for course in courses:
        print("ID: {}, name: {}" .format(course['id'], course['name']))

def listStudents(students):
    print("\nStudent List")
    for student in students:
        print("ID: {}, name: {}, dob: {}" .format(student['id'], student['name'], student['dob']))

def inputMarks(students, courses, marks):
    listCourses(courses)
    print("Enter course ID: ")
    course = input()
    if course not in marks:
        marks[course] = {}
    listStudents(students)
    print("Enter student ID for mark: ")
    student = input()
    marks[course][student] = float(input("Enter mark: "))
    return marks

def showMarks(students, marks):
    course = input("Choose course: ")
    
    if course not in marks or marks[course] == {}:
        print("TBD")
    else:
        for student in students:
            if (student["id"] in marks[course]):
                print("ID: {}, Mark: {}".format(student["id"], marks[course][student["id"]]))
            else:
                print("ID: {}, Mark: TBD".format(student["id"]))
marks = {}
while (True):
    print("CHOOSE: ")
    print("0. Exit now")
    print("1. Input students")
    print("2. Input courses")
    print("3. List courses")
    print("4. List students")
    print("5. Input mark")
    print("6. Show mark\n")

    choice = int(input())
    if (choice == 0):
        break
    elif (choice == 1):
        students = StudentNo()
    elif (choice == 2):
        courses = CourseNo()
    elif (choice == 3):
        listCourses(courses)
    elif (choice == 4):
        listStudents(students)
    elif (choice == 5):
        marks = inputMarks(students,courses, marks)
    elif (choice == 6):
        showMarks(students, marks)
    else:
        print("Invalid")