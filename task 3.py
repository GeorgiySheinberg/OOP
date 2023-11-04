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
                f'{middle_rate(self.grades)}\nКурсы в процессе '
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
                f'{middle_rate(self.lecture_estimates)}')


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


def compare_students(first, second, third):
    if first >= second:
        if first >= third:
            return print(f'Лучший студент {student_1.surname} {student_1.name} c результатом: {first}')
        else:
            return print(f'Лучший студент {student_3.surname} {student_1.name} c результатом: {third}')
    elif second >= third:
        if second >= third:
            return print(f'Лучший студент {student_2.surname} {student_1.name} c результатом: {second}')
        else:
            return print(f'Лучший студент {student_3.surname} {student_1.name} c результатом: {third}')
    else:
        return "ERROR"


def middle_rate(dictionary):
    a = 0
    count = 0
    for key in dictionary:
        for value in dictionary.get(key):
            a += int(value)
            count += 1
    return str(a / count)


def compare_lecturers(first, second):
    if first >= second:
        return print(f'Лучший лектор {lecturer_1.surname} {lecturer_1.name} с результатом {first}')
    else:
        return print(f'Лучший лектор {lecturer_2.surname} {lecturer_2.name} с результатом {second}')


# Наполняем данными:
student_1 = Student('Smirnov', 'Igor', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.courses_in_progress += ['Fullstack']

student_2 = Student('Ivanov', 'Ivan', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.courses_in_progress += ['Fullstack']

student_3 = Student('Petrov', 'Petr', 'your_gender')
student_3.courses_in_progress += ['Fullstack']
student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['Java']

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

reviewer_1.rate_hw(student_3, 'Python', 6)
reviewer_1.rate_hw(student_3, 'Python', 2)
reviewer_1.rate_hw(student_3, 'Python', 1)
reviewer_1.rate_hw(student_3, 'Java', 4)
reviewer_1.rate_hw(student_3, 'Java', 3)
reviewer_1.rate_hw(student_3, 'Java', 9)
reviewer_1.rate_hw(student_3, 'Fullstack', 7)
reviewer_1.rate_hw(student_3, 'Fullstack', 9)


# Оценки за лекции(лекторы ведут по 1 курсу):
lecturer_1 = Lecturer('Clever', 'Person')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Smart', 'Human')
lecturer_2.courses_attached += ['Java']

student_1.rate_lt(lecturer_1, 'Python', 10)
student_2.rate_lt(lecturer_1, 'Python', 9)
student_3.rate_lt(lecturer_1, 'Python', 8)

student_1.rate_lt(lecturer_2, 'Java', 6)
student_2.rate_lt(lecturer_2, 'Java', 8)
student_3.rate_lt(lecturer_2, 'Java', 5)

print("Студенты:")
print(student_1.grades)
print()
print(student_2.grades)
print()
print(student_3.grades)
print()
print(student_1)
print()
print(student_2)
print()
print(student_3)
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

compare_students(middle_rate(student_1.grades), middle_rate(student_2.grades),
                 middle_rate(student_3.grades))
compare_lecturers(middle_rate(lecturer_1.lecture_estimates), middle_rate(lecturer_2.lecture_estimates))
