from django.db import models
from .cohort import Cohort

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    slack_handle = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("instructor")
        verbose_name_plural = ("instructors")

    # def __str__(self):
    #     return self.name


