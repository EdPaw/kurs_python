class Student:
    school = 'uam'

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def email(self):
        return f'{self.first[0]}.{self.last}@{self.school}.pl'

    def sound(self, number):
        return f'go {self.school}!' * number


anna = Student('anna', 'nowak', 23)

print(anna.email())
print(anna.sound(3))

print(anna.__dict__)
