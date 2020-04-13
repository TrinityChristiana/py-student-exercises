# Name of exercise
# Language of exercise (JavaScript, Python, CSharp, etc.)

from factory import class_maker
ExerciseInit = class_maker("ExerciseInit", ["name", "language"])

class Exercise(ExerciseInit):
    def this_method(self):
        print(self)        