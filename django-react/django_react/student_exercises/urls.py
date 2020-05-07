from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('cohort', views.CohortListCreate) 
router.register('student', views.StudentListCreate)
router.register('exercise', views.ExerciseListCreate)
router.register('instructor', views.InstructorListCreate)
router.register('student-exercise', views.StudentExerciseCreate)

urlpatterns = [
    path('api/', include(router.urls) ),
]