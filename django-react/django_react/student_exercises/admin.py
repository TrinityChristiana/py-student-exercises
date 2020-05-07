from django.contrib import admin
from .models import StudentExercise, Cohort, Student, Exercise, Instructor
# Register your models here.

admin.site.register(StudentExercise)
admin.site.register(Cohort)
admin.site.register(Student)
admin.site.register(Exercise)
admin.site.register(Instructor)
