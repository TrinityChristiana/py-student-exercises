from ...models import StudentExercise
from ...serializers import StudentExerciseSerializer
from rest_framework import viewsets

class StudentExerciseCreate(viewsets.ModelViewSet):
    queryset = StudentExercise.objects.all()
    serializer_class = StudentExerciseSerializer