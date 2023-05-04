class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __avg_rating(self, some_student):
        rating_counter = 0
        rating_sum = 0
        for course, grade in some_student.grades.items():
            rating_counter += len(grade)
            rating_sum += sum(grade)
        res = round(rating_sum / rating_counter, 2)
        return res
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__avg_rating(self)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
    
    def __lt__(self, other):
        return self.__avg_rating(self) < self.__avg_rating(other)
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __avg_rating(self, some_lecturer):
        rating_counter = 0
        rating_sum = 0
        for course, grade in some_lecturer.grades.items():
            rating_counter += len(grade)
            rating_sum += sum(grade)
        res = round(rating_sum / rating_counter, 2)
        return res
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__avg_rating(self)}'
        return res

    def __lt__(self, other):
        return self.__avg_rating(self) < self.__avg_rating(other)

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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def avg_rating_hw(students, course):
    rating_counter = 0
    rating_sum = 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            rating_counter += len(student.grades[course])
            rating_sum += sum(student.grades[course])
        else:
            return 'Ошибка'
    res = round(rating_sum / rating_counter, 2)
    return res

def avg_rating_l(lecturers, course):
    rating_counter = 0
    rating_sum = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            rating_counter += len(lecturer.grades[course])
            rating_sum += sum(lecturer.grades[course])
        else:
            return 'Ошибка'
    res = round(rating_sum / rating_counter, 2)
    return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

not_so_best_student = Student('Puoy', 'Yman', 'your_gender')
not_so_best_student.courses_in_progress += ['Python', 'Git']
not_so_best_student.finished_courses += ['Введение в программирование']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(not_so_best_student, 'Python', 8)
cool_reviewer.rate_hw(not_so_best_student, 'Python', 8)
cool_reviewer.rate_hw(not_so_best_student, 'Python', 6)
 
second_reviewer = Reviewer('Some3', 'Buddy3')
second_reviewer.courses_attached += ['Git']
 
second_reviewer.rate_hw(best_student, 'Git', 10)
second_reviewer.rate_hw(best_student, 'Git', 9)
second_reviewer.rate_hw(best_student, 'Git', 10)

second_reviewer.rate_hw(not_so_best_student, 'Git', 9)
second_reviewer.rate_hw(not_so_best_student, 'Git', 7)
second_reviewer.rate_hw(not_so_best_student, 'Git', 6)

print(best_student.grades)
print(not_so_best_student.grades)
print()

cool_lecturer = Lecturer('Some1', 'Buddy1')
cool_lecturer.courses_attached += ['Python']

best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 10)

not_so_best_student.rate_hw(cool_lecturer, 'Python', 9)
not_so_best_student.rate_hw(cool_lecturer, 'Python', 10)
not_so_best_student.rate_hw(cool_lecturer, 'Python', 10)

second_lecturer = Lecturer('Some2', 'Buddy2')
second_lecturer.courses_attached += ['Git']

best_student.rate_hw(second_lecturer, 'Git', 10)
best_student.rate_hw(second_lecturer, 'Git', 9)
best_student.rate_hw(second_lecturer, 'Git', 8)

not_so_best_student.rate_hw(second_lecturer, 'Git', 8)
not_so_best_student.rate_hw(second_lecturer, 'Git', 9)
not_so_best_student.rate_hw(second_lecturer, 'Git', 10)

print(best_student)
print()
print(not_so_best_student)
print()
print(cool_reviewer)
print()
print(second_reviewer)
print()
print(cool_lecturer)
print()
print(second_lecturer)
print()
print(best_student > not_so_best_student)
print()
print(cool_lecturer > second_lecturer)
print()
print(f'Средняя оценка за домашние задания по курсу: {avg_rating_hw([best_student, not_so_best_student], "Python")}')
print()
print(f'Средняя оценка за лекции по курсу: {avg_rating_l([cool_lecturer], "Python")}')