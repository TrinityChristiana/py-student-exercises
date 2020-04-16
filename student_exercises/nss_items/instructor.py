import json
from .nss_person import NSSPerson
class Instructor(NSSPerson):
    def __init__(self, first_name, last_name,  slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty

    def add_stu_to_exer(self, exercise_instance, student_instance):
        student_instance.exercises_list.append(exercise_instance)
        

    def print_details(self):
        print(json.dumps(self.__dict__, indent=2))