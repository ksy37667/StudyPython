# 기본 인스턴스 메소드

class Student(object):
    """
    Student Class
    Author : Lee
    Date : 2020.01.07
    Description : Class, Static, Instance Method
    """

    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._grade = grade
        self._email = email
        self._tuition = tuition
        self._gpa = gpa

    
    # Instance Method

    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    def get_fee(self):
        return 'Before Tuition -> Id : {}, fee: {}'.format(self._id, self._tuition)

    def get_fee_culc(self):
        return 'After tuition -> Id : {}, fee: {}'.format(self._id, self._tuition * Student.tuition_per)

    def __str__(self):
        return 'Student Info \n name: {} \n grade: {} \n email: {} \n'.format(self.full_name(), self._grade, self._email)


    # Class Method
    
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.tuition_per = per
        print('Succeed Method')

    #Class Method

    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient.'



student_1 = Student(1, 'Kim', 'Sarang', 'ksy37667@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'Student2@daum.net', '2', 500, 4.3)

print(student_1)
print(student_2)

print()

# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())


# 학비 정보 (인상전)
print(student_1.get_fee())
print(student_2.get_fee())

print()

# 학비 인상(클래스 메소드 미사용)
# Student.tuition_per = 1.2

Student.raise_fee(1.5)
# 학비 정보 (인상후)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
print()


# 클래스 메소드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Park', 'Minji', 'Student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'Sunghan', 'Student3@gmail.com', '3', 600, 4.1)

print(student_3.detail_info())
print(student_4.detail_info())

print()


# 학생 학비 변경 확인

print(student_3._tuition)
print(student_4._tuition)
print()

# 장학금 혜택 여부(static 메소드 미사용)

def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient.'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

print()

# 장학금 혜택 여부(static 메소드 사용)

print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print()

print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))
