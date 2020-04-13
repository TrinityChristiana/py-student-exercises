from factory import class_maker
# Properties
# First name
# Last name
# Slack handle
# The student's cohort
# The collection of exercises that the student is currently working on

StudentInit = class_maker("StudentInit", ["first_name", "last_name", "slack_handle", "cohort_instance", "exercises_instances"], ["asadsasd"])

class Student(StudentInit):
    def this_method(self):
        pass
