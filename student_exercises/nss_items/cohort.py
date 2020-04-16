import json

class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()

    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def print_details(self):
        new_dict = self.__dict__
        new_list = list()
        for student in new_dict["students"]:
            new_list.append(student.__dict__)
        new_dict["students"] = new_list

        inst_list = list()
        for instructor in new_dict["instructors"]:
            inst_list.append(instructor.__dict__)
        new_dict["instructors"] = inst_list

        print(json.dumps(new_dict, indent=2))
