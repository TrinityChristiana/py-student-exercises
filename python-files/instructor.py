# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student

from factory import class_maker
InstructorInit = class_maker("InstructorInit", ["first_name", "last_name", "slack_handle", "cohort_instance", "specialty"])

class Instructor(InstructorInit):
    def add_stu_to_exer(self, exercise_instance, student_instance):
        self.exercise_instance = exercise_instance
        self.student_instance = student_instance
