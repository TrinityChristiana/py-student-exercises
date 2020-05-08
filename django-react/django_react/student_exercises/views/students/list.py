from ...models import Student, Cohort
from ...serializers import StudentSerializer, Error, ErrorSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Prefetch
from django.shortcuts import render
from django.db.models.expressions import RawSQL



class StudentListCreate(viewsets.ModelViewSet):
    # model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    # def list(self, response):
    #     queryset, serializer = self.get_queryset()
    #     return Response(serializer.data)

    # def get_queryset(self):
    #     queryset = Student.objects.all()

    #     _embed = self.request.query_params.get('_embed', None)
    #     print(queryset)
    #     serializer = StudentSerializer(queryset, many=True)

    #     # if _embed:
    #     #     sqlquery = ("""
    #     #                 SELECT 
    #     #                     c.name cohort 
    #     #                 FROM student_exercises_student s
    #     #                 JOIN student_exercises_cohort c
    #     #                 ON c.id = s.cohort
    #     #                 """)
    #     #     Student.objects.extra(select={"cohort": sqlquery})

    #     #     print(Student.objects.values())
    #     #     embed_on = _embed.split(",")
            
 
    #     return queryset, serializer
