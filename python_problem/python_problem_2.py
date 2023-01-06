

# ==================== Class =======================

class Student():
    student_name = []

    def __init__(self, name, mid, final):
        self.name = name
        self.mid = mid
        self.final = final
        self.grade = -1
        self.student_name.append(name)

    @staticmethod
    def check_name_exists(new_name):
        names = Student.student_name
        for name in names:
            if name == new_name:
                return True
        return False


class StudentList():
    student_list = []

    # 학생 정보를 저장하는 함수
    @staticmethod
    def push(student):
        StudentList.student_list.append(student)


# ================== functions ======================

def Menu1(name, mid, final):
    temp = Student(name, mid, final)
    StudentList.push(dict(name=name, mid=mid, final=final, grade=-1))


def Menu2():
    for student in StudentList.student_list:
        if student['grade'] == -1:
            avg = (student['mid'] + student['final']) / 2
            if avg >= 90:
                student['grade'] = 'A'
            elif avg >= 80:
                student['grade'] = 'B'
            elif avg >= 70:
                student['grade'] = 'C'
            else:
                student['grade'] = 'D'


def Menu3():
    print('------------------------------')
    print('name\tmid\tfinal\tgrade')
    print('------------------------------')
    for student in StudentList.student_list:
        name = student['name']
        mid = student['mid']
        final = student['final']
        grade = student['grade']
        print(f'{name}\t{mid}\t{final}\t{grade}')


def Menu4(name):
    # 1) student_name pop
    Student.student_name.remove(name)
    # 2) student list pop
    idx = 0
    for i, v in enumerate(StudentList.student_list):
        if name == v['name']:
            idx = i
    del StudentList.student_list[idx]


print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            name, mid, final = input(
                "Enter name mid-score final-score : ").split()

            # 동일한 이름 여부 처리
            if Student.check_name_exists(name):
                raise Exception("Already exist name!")

            # 정수 입력 처리
            if not mid.isdigit() or not final.isdigit() or int(mid) <= 0 or int(final) <= 0:
                raise Exception("scores must be integer!")

            Menu1(name, int(mid), int(final))

        # 데이터 개수 처리
        except ValueError as e:
            print("Num of data is not 3!")
        except Exception as e:
            print(e)

    elif choice == "2":
        try:
            if len(StudentList.student_list) == 0:
                raise Exception("No student data!")

            Menu2()
            print("Grading to all students.")
        except Exception as e:
            print(e)

    elif choice == "3":
        try:
            if len(StudentList.student_list) == 0:
                raise Exception("No student data!")

            for i in StudentList.student_list:
                if i['grade'] == -1:
                    raise Exception("There is a student who didn't get grade.")
            Menu3()
        except Exception as e:
            print(e)

    elif choice == "4":
        try:
            if len(StudentList.student_list) == 0:
                raise Exception("No student data!")

            name = input("Enter the name to delete : ")

            if name not in Student.student_name:
                raise Exception("Not exist name!")

            # 삭제
            Menu4(name)
            print(f"{name} student information is deleted.")
        except Exception as e:
            print(e)

    elif choice == "5":
        print("Exit Program!")
        break

    else:
        print("Wrong number. Choose again.")
