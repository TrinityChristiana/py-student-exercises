from ...models import Cohort
from ...serializers import CohortSerializer
from rest_framework import viewsets

class CohortListCreate(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer