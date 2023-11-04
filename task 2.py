class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lt(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.lecture_estimates:
                lecturer.lecture_estimates[course] += [grade]
            else:
                lecturer.lecture_estimates[course] = [grade]
        else:
            return print('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_estimates = {}
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Оценка студентам:
student_1 = Student('Smirnov', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']

student_2 = Student('Ivanov', 'Ivan', 'your_gender')
student_2.courses_in_progress += ['Java']

student_3 = Student('Petrov', 'Petr', 'your_gender')
student_3.courses_in_progress += ['Fullstack']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Some', 'Buddy')
reviewer_2.courses_attached += ['Java']

reviewer_3 = Reviewer('Some', 'Buddy')
reviewer_3.courses_attached += ['Fullstack']

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_3.rate_hw(student_3, 'Fullstack', 9)

print(student_1.grades)
print(student_2.grades)
print(student_3.grades)

# Оценки за лекции:
lecturer_1 = Lecturer('Clever', 'Person')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Clever', 'Person')
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Clever', 'Person')
lecturer_3.courses_attached += ['Fullstack']

student_1.rate_lt(lecturer_1, 'Python', 10)
student_2.rate_lt(lecturer_2, 'Java', 9)
student_3.rate_lt(lecturer_3, 'Fullstack', 8)

print(lecturer_1.lecture_estimates)
print(lecturer_2.lecture_estimates)
print(lecturer_3.lecture_estimates)
