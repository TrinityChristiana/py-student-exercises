from django.db import models
from .cohort import Cohort

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    slack_handle = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("student")
        verbose_name_plural = ("students")

    # def __str__(self):
    #     return self.name


