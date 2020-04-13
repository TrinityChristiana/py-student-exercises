# The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)
# The collection of students in the cohort.
# The collection of instructors in the cohort.

from factory import class_maker
CohortInit = class_maker("CohortInit", ["name", "students", "instructors"])


class Cohort(CohortInit):
    def add_student(self, student):
        self.students.append(student)
