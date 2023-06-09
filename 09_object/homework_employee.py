class Employee:

    company = "Love Python Company"

    def __init__(self, position, salary, name, surname, work_experience, is_student):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.work_experience = work_experience
        self.is_student = is_student

    def get_email(self):
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        result = []
        text = self.name + self.surname
        for char in text:
            if char in consonants:
                result.append(char)

        first_part = ''.join(result).lower()
        second_part = self.company.lower().replace(" ", "")
        mail = first_part + '@' + second_part + ".com"

        return mail

    def salary_raise(self, position_change, phase_of_the_moon):
        if position_change and phase_of_the_moon == "full moon":
            self.salary += self.salary * 0.2
        elif position_change:
            self.salary += self.salary * 0.1
        else:
            self.salary += self.salary * 0.05

    def calculate_tax(self):
        income_tax = self.salary * 0.19
        if self.is_student:
            health_care = self.salary * 0
        else:
            health_care = self.salary * 0.05

        tax = income_tax + health_care

        return tax

    def show_employee_details(self):
        return print(f"{self.name} {self.surname}. {self.position}, {self.work_experience} of work experience. "
                f"Salary: {self.salary}. Is student: {self.is_student}")


adam_kowalski = Employee("junior", 8000, "Adam", "Kowalski", "2 years", True)
anna_nowak = Employee("mid", 15000, "Anna", "Nowak", "4 years", False)

print(adam_kowalski.get_email())
print(anna_nowak.get_email())

adam_kowalski.show_employee_details()
anna_nowak.show_employee_details()

print(f"Tax is: {adam_kowalski.calculate_tax()}")
print(f"Tax is: {anna_nowak.calculate_tax()}")

adam_kowalski.salary_raise(True, "full moon")
anna_nowak.salary_raise(False, "third quarter")

adam_kowalski.show_employee_details()
anna_nowak.show_employee_details()

print(f"Tax is: {adam_kowalski.calculate_tax()}")
print(f"Tax is: {anna_nowak.calculate_tax()}")
