class Grade:
    def __int__(self, name, grade):
        self.name = name
        self.grade = grade

grade1 = Grade("Steven", 123)

print(grade1.name, grade1.grade)