class Mentor:
    '''Создаётся родительский класс преподавателей'''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    '''Создаётся класс преподавателей, читающих лекции студентам'''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_lect_score = 0

    def __str__(self):
        return (f'\nИмя: {self.name} \nФамилия: {self.surname}')


class Student:
    '''Создаётся класс студентов, обучающихся на курсах и оценивающих лекции'''
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectur(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade >= 0 and grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]

                else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'\nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}')


class Reviewer(Mentor):
    '''Создаётся класс преподавателей, проверяющих и оценивающих домашние работы студентов'''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade >= 0 and grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}'

def lect_score(lecturer):
    '''РАСЧЁТ СРЕДНЕГО БАЛЛА ОЦЕНОК ЗА ЛЕКЦИИ ПРЕПОДАВАТЕЛЯМ ОТ СТУДЕНТОВ'''
    ratings = []
    for value in lecturer.grades.values():
        ratings += value
        if len(ratings) != 0:
            average_score = (sum(ratings)/len(ratings))
    print (f'Средний балл: {round(average_score, 1)}')



def student_score(student):
    '''РАСЧЁТ СРЕДНЕГО БАЛЛА ОЦЕНОК ЗА ДОМАШНИЕ ЗАДАНИЯ СТУДЕНТАМ ОТ ПРОВЕРЯЮЩИХ ПРЕПОДАВАТЕЛЕЙ'''
    ratings = []
    for value in student.grades.values():
        ratings += value
        if len(ratings) != 0:
            average_score = (sum(ratings)/len(ratings))
    print (f'Средний балл: {round(average_score, 1)}')

def lect_score(lecturer):
    '''ЛУЧШИЙ ЛЕКТОР НА КУРСЕ'''
    ratings = []
    for value in lecturer.grades.values():
        ratings += value
        if len(ratings) != 0:
            average_score = (sum(ratings)/len(ratings))
    print (f'Средний балл: {round(average_score, 1)}')


# Проверка работоспособности кода

'''Создаются экземпляры классов: лекторы, студенты и проверяющие'''

lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Python', 'Git', 'HTML и CSS']
lecturer_2 = Lecturer('Тимур', 'Сейсембаев')
lecturer_2.courses_attached += ['Python', 'ООП и работа c API', 'HTML и CSS']

student_1 = Student('Дмитрий', 'Медведкин', 'муж')
student_1.courses_in_progress += ['Python', 'Git', 'HTML и CSS']
student_1.finished_courses += ['Введение в программирование', 'ООП и работа c API']
student_1.rate_lectur(lecturer_1, 'Git', 10)
student_1.rate_lectur(lecturer_1, 'Python', 10)
student_1.rate_lectur(lecturer_1, 'HTML и CSS', 10)
student_1.rate_lectur(lecturer_2, 'Python', 10)
student_1.rate_lectur(lecturer_2, 'HTML и CSS', 10)

student_2 = Student('Владимир', 'Путев', 'муж')
student_2.courses_in_progress += ['Python', 'Git', 'ООП и работа c API']
student_2.finished_courses += ['Введение в программирование']
student_2.rate_lectur(lecturer_1, 'Git', 10)
student_2.rate_lectur(lecturer_1, 'Python', 8)
student_2.rate_lectur(lecturer_2, 'Python', 9)
student_2.rate_lectur(lecturer_2, 'ООП и работа c API', 9)

reviewer_1 = Reviewer('Алёна', 'Батицкая')
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 10)

reviewer_2 = Reviewer('Иван', 'Бочаров')
reviewer_2.courses_attached += ['Python', 'ООП и работа c API', 'HTML и CSS',]
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'HTML и CSS', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'ООП и работа c API', 10)

print(lecturer_1)
lect_score(lecturer_1)

print(lecturer_2)
lect_score(lecturer_2)

print(student_1)
student_score(student_1)

print(student_2)
student_score(student_2)

