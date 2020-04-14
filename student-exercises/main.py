from cohort import Cohort
from exercise import Exercise
from student import Student
from instructor import Instructor
import random
# from trinity_helper.print import collection

# Create 4, or more, exercises.
exercise_list = (["Pizza Joint", "python"], ["Urban Planner", "python"], [
                 "Companies and Employees", "python"], ["Urban Planner II", "python"])

exercise_dictonary = dict()

for [name, language] in exercise_list:
    exercise_dictonary[name] = Exercise(name, language)

# Create 3, or more, cohorts.
cohort_list = ["Cohort 35","Cohort 38", "Cohort 40"]

cohort_dictonary = dict()

for name in cohort_list:
    cohort_dictonary[name] = Cohort(name)


# Create 4, or more, students and assign them to one of the cohorts.
student_list = (
    ["Alyssa", "Nycum", "Alyssa Nycum", "Cohort 38"],
    ["Katie", "Wohlm", "Katie Wohlm", "Cohort 38"],
    ["Mollie", "Goforth", "Mollie", "Cohort 38"],
    ["Roxanne", "Nasraty", "Roxanne", "Cohort 40"],
    ["Sofia", "Candiani", "Sofiancandiani", "Cohort 38"],
    ["Trinity", "Terry", "Trinity", "Cohort 38"],
    ["Keaton", "Williamson", "keatonwilliamson", "Cohort 35"],
    ["Matthew", "Kroeger", "Matthew Kroger", "Cohort 38"],
)

student_dictonary = dict()

for [first_name, last_name, slack_handle, cohort_name] in student_list:
    student_dictonary[slack_handle] = Student(first_name, last_name, slack_handle, cohort_name)
    cohort_dictonary[cohort_name].add_student(student_dictonary[slack_handle])



# # [[print(student) for student in cohort_dictonary[cohort].students] for cohort in cohort_dictonary]

# # Create 3, or more, instructors and assign them to one of the cohorts.
# # ["first_name", "last_name", "slack_handle", "cohort_instance", "specialty"]

instructor_list = (
    ["Bryan", "Nilsen", "Bryan Nilsen", "Cohort 40", "Hi-Fives"],
    ["Andy", "Collins", "andyc", "Cohort 38", "Knowledge"],
    ["Kristen", "Noriss","kristen.norris", "Cohort 38", "Helping"],
    ["Chase", "Fire", "Chase Fite", "Cohort 38", "Listening"],
    ["Jisie", "David", "jisie", "Cohort 38", "Teaching"]
)

instructor_dictionary = dict()

for [first_name, last_name, slack_handle, cohort_name, specialty] in instructor_list:
    instructor_dictionary[slack_handle] = Instructor(first_name, last_name, slack_handle, cohort_name, specialty)
    cohort_dictonary[cohort_name].add_instructor(instructor_dictionary[slack_handle])

exercise_picker = list(map(lambda name: name[1], exercise_dictonary.items()))

for (inst_name, inst_value) in instructor_dictionary.items():
    for i in range(2):
        for (stu_name, stu_value) in student_dictonary.items():
            inst_value.add_stu_to_exer(random.choice(exercise_picker), stu_value)
        

# for (key, value) in cohort_dictonary.items():
#     value.print_details()
# 
# student_dictonary["Trinity"].print_details()
# for (key, value) in student_dictonary.items():
#     value.print_details()

# for (key, value) in instructor_dictionary.items():
#     value.print_details()

# for (key, value) in exercise_dictonary.items():
#     value.print_details()


for (hash, value) in student_dictonary.items():
    stu_dict = value.__dict__
    exercises = stu_dict["exercises_list"]
    new_set = set()
    for exercise in exercises:
        new_set.add(exercise.__dict__["name"])
    list_of_exercises = ", and ".join([", ".join(list(new_set)[:-1]),list(new_set)[-1]] if len(list(new_set)) > 2 else list(new_set))
    print(f"{stu_dict['first_name']} is working on {list_of_exercises}")
    
