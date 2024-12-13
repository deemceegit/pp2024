class Person:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self._dob = dob

    @property
    def dob(self):
        return self._dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}"

class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class USTH:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}

    def add_student(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        dob = input("Enter DOB: ")
        self._students.append(Student(id, name, dob))

    def add_course(self):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        self._courses.append(Course(id, name))

    def list_students(self):
        print("\nStudent List:")
        for student in self._students:
            print(student)

    def list_courses(self):
        print("\nCourse List:")
        for course in self._courses:
            print(course)

    def input_mark(self):
        self.list_courses()
        course_id = input("Enter course ID: ")
        course = next((c for c in self._courses if c.id == course_id), None)

        if not course:
            print("Invalid course ID")
            return

        if course_id not in self._marks:
            self._marks[course_id] = {}

        self.list_students()
        student_id = input("Enter student ID: ")
        student = next((s for s in self._students if s.id == student_id), None)

        if not student:
            print("Invalid student ID")
            return

        mark = float(input("Enter mark: "))
        self._marks[course_id][student_id] = mark

    def show_marks(self):
        self.list_courses()
        course_id = input("Choose course ID: ")
        course = next((c for c in self._courses if c.id == course_id), None)

        if not course or course_id not in self._marks:
            print("TBD")
            return

        print(f"\nMarks for course {course.name}:")
        for student in self._students:
            mark = self._marks[course_id].get(student.id, "TBD")
            print(f"ID: {student.id}, Name: {student.name}, Mark: {mark}")

    def run(self):
        while True:
            print("CHOOSE: ")
            print("0. Exit now")
            print("1. Input students")
            print("2. Input courses")
            print("3. List courses")
            print("4. List students")
            print("5. Input mark")
            print("6. Show mark\n")

            choice = int(input("Your choice: "))

            if choice == 0:
                break
            elif choice == 1:
                self.add_student()
            elif choice == 2:
                self.add_course()
            elif choice == 3:
                self.list_courses()
            elif choice == 4:
                self.list_students()
            elif choice == 5:
                self.input_mark()
            elif choice == 6:
                self.show_marks()
            else:
                print("Invalid choice")

usth = USTH()
usth.run()