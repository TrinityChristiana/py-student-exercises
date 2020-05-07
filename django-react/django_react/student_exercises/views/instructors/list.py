from ...models import Instructor
from ...serializers import InstructorSerializer
from rest_framework import viewsets

class InstructorListCreate(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer