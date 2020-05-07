from django.db import models
from .student import Student
from .exercise import Exercise
from .instructor import Instructor

class StudentExercise(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("student_exercise")
        verbose_name_plural = ("student_exercises")

    # def __str__(self):
    #     return self.name


