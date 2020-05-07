from ...models import Exercise
from ...serializers import ExerciseSerializer
from rest_framework import viewsets

class ExerciseListCreate(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer