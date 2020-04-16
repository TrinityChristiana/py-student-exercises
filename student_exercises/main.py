# **************************** Challenge: Student Exercises ****************************
"""
Author: Trinity Terry
pyrun: python main.py
"""

from nss_items import Cohort
from nss_items import Exercise
from nss_items import Student
from nss_items import Instructor
import random

def make_exercise_instances(tuple_it):
    """
    Creates Exercise Instances from Tuple of Lists

    tuple_it -- tuple of lists ["name_of_exercise", "language_of_exercise"]

    returns: dictionary {"name_of_exercise": <exercise.Exercise object at XxXXXXXXXXX>}
    """
    exercise_dictonary = dict()
    for [name, language] in tuple_it:
        exercise_dictonary[name] = Exercise(name, language)
    return(exercise_dictonary)

def make_cohort_instances(list_it):
    """
    Creates Cohort Instances from List

    list_it -- lists ["name_of_cohort"]

    returns: dictionary {"name_of_cohort": <cohort.Cohort object at XxXXXXXXXXX}
    """
    new_dict = dict()
    for name in cohort_list:
        new_dict[name] = Cohort(name)
    return(new_dict)

def make_student_instances(tuple_it):
    """
    Creates Student Instances from Tuple of Lists

    tuple_int -- Tuple of Lists ["first_name", "last_name", "slack_handle", "cohort_name]

    returns: dictionary {"slack_handle":  <student.Student object at XxXXXXXXXXX}
    """

    new_dict = dict()
    for [first_name, last_name, slack_handle, cohort_name] in tuple_it:
        new_dict[slack_handle] = Student(first_name, last_name, slack_handle, cohort_name)
        cohort_dictonary[cohort_name].add_student(new_dict[slack_handle])
    return new_dict

def make_instructor_instances(tuple_it):

    """
    Creates Instructor Instances from Tuple of Lists

    tuple_int -- Tuple of Lists ["first_name", "last_name", "slack_handle", "cohort_name", "specialty"]

    returns: dictionary {"slack_handle":  <instructor.Instructor object at XxXXXXXXXXX}
    """

    new_dict = dict()

    for [first_name, last_name, slack_handle, cohort_name, specialty] in tuple_it:
        new_dict[slack_handle] = Instructor(first_name, last_name, slack_handle, cohort_name, specialty)
        cohort_dictonary[cohort_name].add_instructor(new_dict[slack_handle])
    return new_dict
    return new_dict

# Holds List of exercises that will be iterated over to create Exercise Instances
exercise_tuple = (["Pizza Joint", "python"], ["Urban Planner", "python"], [
                 "Companies and Employees", "python"], ["Urban Planner II", "python"])
exercise_dictonary = make_exercise_instances(exercise_tuple)

# Holds List of Cohort Names that will be iterated over to create Cohort Instances
cohort_list = ["Cohort 35","Cohort 38", "Cohort 40"]
cohort_dictonary = make_cohort_instances(cohort_list)

# Holds Tuple of Student Lists that will be iterated over to create Student Instances
student_tuple = (
    ["Alyssa", "Nycum", "Alyssa Nycum", "Cohort 38"],
    ["Katie", "Wohlm", "Katie Wohlm", "Cohort 38"],
    ["Mollie", "Goforth", "Mollie", "Cohort 38"],
    ["Roxanne", "Nasraty", "Roxanne", "Cohort 40"],
    ["Sofia", "Candiani", "Sofiancandiani", "Cohort 38"],
    ["Trinity", "Terry", "Trinity", "Cohort 38"],
    ["Keaton", "Williamson", "keatonwilliamson", "Cohort 35"],
    ["Matthew", "Kroeger", "Matthew Kroger", "Cohort 38"],
)
student_dictonary = make_student_instances(student_tuple)

# Holds Tuple of Insructor Lists that will be iterated over to create Insructor Instances
instructor_list = (
    ["Bryan", "Nilsen", "Bryan Nilsen", "Cohort 40", "Hi-Fives"],
    ["Andy", "Collins", "andyc", "Cohort 38", "Knowledge"],
    ["Kristen", "Noriss","kristen.norris", "Cohort 38", "Helping"],
    ["Chase", "Fire", "Chase Fite", "Cohort 38", "Listening"],
    ["Jisie", "David", "jisie", "Cohort 38", "Teaching"]
)
instructor_dictionary = make_instructor_instances(instructor_list)

# List of exercise names
exercise_picker = list(map(lambda name: name[1], exercise_dictonary.items()))

# For each instructor assign each student two random assignmants
for (inst_name, inst_value) in instructor_dictionary.items():
    for i in range(2):
        for (stu_name, stu_value) in student_dictonary.items():
            # random.choice picks random exercise
            inst_value.add_stu_to_exer(random.choice(exercise_picker), stu_value)


# For Each Student, list all exercises thay were assigned
for (hash, value) in student_dictonary.items():
    stu_dict = value.__dict__
    exercises = stu_dict["exercises_list"]
    # Using a set instead of a list to collect so there are no duplicates

    new_set = set()
    for exercise in exercises:
        new_set.add(exercise.__dict__["name"])
    list_of_exercises = ", and ".join([", ".join(list(new_set)[:-1]),list(new_set)[-1]] if len(list(new_set)) > 2 else list(new_set))
    print(f"{stu_dict['first_name']} is working on {list_of_exercises}")
    
