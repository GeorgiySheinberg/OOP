class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lt(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.lecture_estimates:
                lecturer.lecture_estimates[course] += [grade]
            else:
                lecturer.lecture_estimates[course] = [grade]
        else:
            return print('Ошибка')

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{avg_rate(self.grades)}\nКурсы в процессе '
                f'изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: Введение в программирование')


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

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:'
                f'{avg_rate(self.lecture_estimates)}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avg_rate(dictionary):
    a = 0
    count = 0
    for key in dictionary:
        for value in dictionary.get(key):
            a += int(value)
            count += 1
    return str(a / count)


def avg_course_mark(students_list, course):  # средняя оценка студентов за курс
    summ = 0
    course_mark_list = []
    for student in students_list:
        for key in student:
            if key == course:
                course_mark_list.extend(student.get(key))
    for mark in course_mark_list:
        summ += mark
    return print(f'Средняя оценка студентов за курс "{course}": {summ / len(course_mark_list)}')


def avg_lecturer_mark(lecturer_list, course):  # средняя оценка лекторов за курс
    summ = 0
    course_mark_list = []
    for student in lecturer_list:
        for key in student:
            if key == course:
                course_mark_list.extend(student.get(key))
    for mark in course_mark_list:
        summ += mark
    return print(f'Средняя оценка лекторов за курс "{course}": {summ / len(course_mark_list)}')


# Наполняем данными:
student_1 = Student('Smirnov', 'Igor', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.courses_in_progress += ['Fullstack']

student_2 = Student('Ivanov', 'Ivan', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.courses_in_progress += ['Fullstack']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Fullstack']

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Java', 7)
reviewer_1.rate_hw(student_1, 'Java', 7)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_1, 'Fullstack', 6)
reviewer_1.rate_hw(student_1, 'Fullstack', 9)

reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Java', 5)
reviewer_1.rate_hw(student_2, 'Java', 3)
reviewer_1.rate_hw(student_2, 'Java', 7)
reviewer_1.rate_hw(student_2, 'Fullstack', 4)
reviewer_1.rate_hw(student_2, 'Fullstack', 9)
# Оценки за лекции(лекторы ведут по 1 курсу):
lecturer_1 = Lecturer('Clever', 'Person')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Smart', 'Human')
lecturer_2.courses_attached += ['Java']

student_1.rate_lt(lecturer_1, 'Python', 10)
student_2.rate_lt(lecturer_1, 'Python', 9)


student_1.rate_lt(lecturer_2, 'Java', 6)
student_2.rate_lt(lecturer_2, 'Java', 8)


print("Студенты:")
print(student_1.grades)
print()
print(student_2.grades)

print()
print(student_1)
print()
print(student_2)
print()
print("Лекторы:")
print(lecturer_1.lecture_estimates)
print()
print(lecturer_1)
print()
print(lecturer_2.lecture_estimates)
print()
print(lecturer_2)
print()
print("Проверяющий:")
print(reviewer_1)
print()

avg_course_mark([student_1.grades, student_2.grades], 'Python')
avg_course_mark([student_1.grades, student_2.grades], 'Java')
avg_course_mark([student_1.grades, student_2.grades], 'Fullstack')
print()

avg_lecturer_mark([lecturer_1.lecture_estimates, lecturer_2.lecture_estimates], 'Python')
avg_lecturer_mark([lecturer_1.lecture_estimates, lecturer_2.lecture_estimates], 'Java')
