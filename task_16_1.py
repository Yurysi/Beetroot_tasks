"""
    School

Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one
called Teacher. Try to find as many methods and attributes as you can which
belong to different classes, and keep in mind which are common and which are
not. For example, the name should be a Person attribute, while salary should
 only be available to the teacher.
"""


class Person:
    def __init__(self, first_name, last_name, institution, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.institution = institution
        self.subject = subject
        info_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "institution": self.institution,
            "subject": self.subject

        }
        self.info_dict = info_dict


class Student(Person):
    def __init__(self, first_name, last_name, institution, subject,
                 num_of_course, tails):
        super().__init__(first_name, last_name, institution, subject)
        self.tails = tails
        self.num_of_course = num_of_course

        self.info_dict.update({'num_of_course': num_of_course, 'tails': tails})


class Teacher(Person):
    def __init__(self, first_name, last_name, institution, subject, chair,
                 salary):
        super().__init__(first_name, last_name, institution, subject)
        self.chair = chair
        self.salary = salary
        self.info_dict.update({'chair': chair, 'salary': salary})


person = Student("Sanya", "Ivanov", "KNUCA", "math", 5, 'English')
print(person.info_dict)
person1 = Teacher("Ivan", "Stepnyak", "KNUCA", "math", "technology", 500)
print(person1.info_dict)