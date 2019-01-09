if __name__ == '__main__':

    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)

    grades = sorted(list(set(map(lambda student: student[1], students))))
    students_with_lowest = [s for s in students if s[1] == grades[1]]

    for s in sorted(students_with_lowest):
        print(s[0])
