from django.db import models
from .cohort import Cohort
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    slack_handle = models.CharField(max_length=50)


    # @property
    # def cohort(self):
    #     print(models.ForeignKey(Cohort, on_delete=models.CASCADE))
    #     print("<django.db.models.fields.related.ForeignKey>")
    #     return models.ForeignKey(Cohort, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("student")
        verbose_name_plural = ("students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




