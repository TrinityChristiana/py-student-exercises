import json

class Instructor():
    def __init__(self, first_name, last_name,  slack_handle, cohort, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.specialty = specialty
        self.cohort = cohort

    def add_stu_to_exer(self, exercise_instance, student_instance):
        student_instance.exercises_list.append(exercise_instance)
        

    def print_details(self):
        print(json.dumps(self.__dict__, indent=2))