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
        self.asc = []

        '''Считает средний балл оценок за лекции'''
        average_score = []
        for score in self.grades.values():
            average_score += score
        if len(average_score) != 0:
            a_s == (sum(average_score)/len(average_score))
            self.asc.append(a_s)
        #else:
        #    return f'оценок нет'

    def __str__(self):
        return (f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grades}'
               f'\n средний балл: {self.asc}')

class Student:
    '''Создаётся класс студентов, обучающихся на курсах'''
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
        return (f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.grades}'
                f'\nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершённые курсы: {self.finished_courses}')

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
print(lecturer_2)

print(student_1)
print(student_2)

print(reviewer_1)
print(reviewer_2)



