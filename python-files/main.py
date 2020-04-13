from cohort import Cohort
from exercise import Exercise
from student import Student
from instructor import Instructor
# ["first_name", "last_name", "slack_handle", "cohort_instance", "specialty"]
import random_thing

# Create 4, or more, exercises.
exercise_list = (["Pizza Joint", "python"], ["Urban Planner", "python"], [
                 "Companies and Employees", "python"], ["Urban Planner II", "python"])

exercise_dictonary = dict()

for [name, language] in exercise_list:
    exercise_dictonary[name] = Exercise(name, language)

# Create 3, or more, cohorts.
cohort_list = (
    ["Cohort 35", list(), list()],
    # ["Cohort 36", list(), list()],
    # ["Cohort 37", list(), list()],
    ["Cohort 38", list(), list()],
    # ["Cohort 39", list(), list()],
    ["Cohort 40", list(), list()],
)

cohort_dictonary = dict()

for [name, student_list, instructor_list] in cohort_list:
    cohort_dictonary[name] = Cohort(name, student_list, instructor_list)


# Create 4, or more, students and assign them to one of the cohorts.
# ["first_name", "last_name", "slack_handle", "cohort_instance", "exercises_instances"]
student_list = (
    ["Alyssa", "Nycum", "Alyssa Nycum", "Cohort 38", list()],
    ["Katie", "Wohlm", "Katie Wohlm", "Cohort 38", list()],
    ["Mollie", "Goforth", "Mollie", "Cohort 38", list()],
    ["Roxanne", "Nasraty", "Roxanne", "Cohort 40", list()],
    ["Sofia", "Candiani", "Sofiancandiani", "Cohort 38", list()],
    ["Trinity", "Terry", "Trinity", "Cohort 38", list()],
    ["Keaton", "Williamson", "keatonwilliamson", "Cohort 35", list()],
    ["Matthew", "Kroeger", "Matthew Kroger", "Cohort 38", list()],
)

student_dictonary = dict()

for [first_name, last_name, slack_handle, cohort_name, exercises_list] in student_list:
    student_dictonary[slack_handle] = Student(
        first_name, last_name, slack_handle, cohort_name, exercises_list)
    cohort_dictonary[cohort_name].add_student(student_dictonary[slack_handle])


print(cohort_dictonary)
# [[print(student) for student in cohort_dictonary[cohort].students] for cohort in cohort_dictonary]

# Create 3, or more, instructors and assign them to one of the cohorts.

# Have each instructor assign 2 exercises to each of the students.
