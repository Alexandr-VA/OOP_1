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
        return (f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредний балл за лекции: {self.average_lect_score}')

    '''Сравнение лекторов по среднему баллу за лекции'''
    def __gt__(self, other):
        if self.average_lect_score > other.average_lect_score:
           return (f'\nЛучший преподаватель: {self.name} {self.surname}'
                   f'\nСредний балл за лекции: {self.average_lect_score}')



class Student:
    '''Создаётся класс студентов, обучающихся на курсах и оценивающих лекции'''
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_homework_score = 0

    def rate_lectur(self, lecturer, course, grade):
        '''Простановка оценок за лекции преподавателям от студентов'''
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade >= 0 and grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        '''Расчёт среднего балла оценок за лекции преподавателям от студентов'''
        ratings = []
        for value in lecturer.grades.values():
            ratings += value
            if len(ratings) != 0:
               average_score = (sum(ratings)/len(ratings))
               lecturer.average_lect_score = round(average_score, 1)

    def __str__(self):
        return (f'\nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}'
                f'\nСредний балл за домашние задания: {self.average_homework_score}')

    '''Сравнение студентов по среднему баллу за домашние задания'''
    def __gt__(self, other):
        if self.average_homework_score > other.average_homework_score:
           return (f'\nЛучший студент: {self.name} {self.surname}'
                   f'\nСредний балл за домашние задания: {self.average_homework_score}')


class Reviewer(Mentor):
    '''Создаётся класс преподавателей, проверяющих и оценивающих домашние работы студентов'''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        '''Простановка оценок за домашние задания студентам от проверяющих преподавателей'''
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade >= 0 and grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        '''Расчёт среднего балла оценок за домашние задания студентам от проверяющих преподавателей'''
        ratings = []
        for value in student.grades.values():
            ratings += value
        if len(ratings) != 0:
           average_score = (sum(ratings)/len(ratings))
           student.average_homework_score = round(average_score, 1)

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}'

def average_lecturers_score_for_course(list_lecturers, course):
    '''Расчёт среднего балла за лекции по курсу'''
    all_average_grade = []
    for person in list_lecturers:
        all_average_grade.extend(person.grades.get(course))
    return f'\nСреддний балл за лекции по курсу {course}: {round(sum(all_average_grade) / len(all_average_grade), 1)}'

def average_students_score_for_course(list_students, course):
    '''Расчёт среднего балла за домашние задания студентов по курсу'''
    all_average_grade = []
    for person in list_students:
        all_average_grade.extend(person.grades.get(course))
    return (f'\nСреддний балл за домашние задания студентов'
           f'\nпо курсу {course}: {round(sum(all_average_grade) / len(all_average_grade), 1)}')

# ПРОВЕРКА РАБОТОСПОСОБНОСТИ КОДА

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
student_1.rate_lectur(lecturer_2, 'Python', 9)
student_1.rate_lectur(lecturer_2, 'HTML и CSS', 10)

student_2 = Student('Владимир', 'Путев', 'муж')
student_2.courses_in_progress += ['Python', 'Git', 'ООП и работа c API']
student_2.finished_courses += ['Введение в программирование']
student_2.rate_lectur(lecturer_1, 'Git', 10)
student_2.rate_lectur(lecturer_1, 'Python', 10)
student_2.rate_lectur(lecturer_2, 'Python', 10)
student_2.rate_lectur(lecturer_2, 'ООП и работа c API', 10)

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

list_lecturers = [lecturer_1, lecturer_2]
average_lecturers_score_for_course = average_lecturers_score_for_course(list_lecturers,'HTML и CSS')

list_students = [student_1, student_2]
average_students_score_for_course = average_students_score_for_course(list_students, 'Python')

'''Вывод результата'''

print(lecturer_1)

print(lecturer_2)

print(student_1)

print(student_2)

print(lecturer_1 > lecturer_2) # Сравнение лекторов по среднему баллу

print(student_1 < student_2) # Сравнение студентов по среднему баллу

print(average_lecturers_score_for_course)

print(average_students_score_for_course)
