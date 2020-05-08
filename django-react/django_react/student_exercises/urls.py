from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('cohort', views.CohortListCreate, basename="cohort") 
router.register('student', views.StudentListCreate, basename="student")
router.register('exercise', views.ExerciseListCreate)
router.register('instructor', views.InstructorListCreate)
router.register('student_exercise', views.StudentExerciseCreate, basename="student_exercise", )

urlpatterns = [
    path('api/', include(router.urls) ),
    # path('^purchases/(?P<username>.+)/$', Student.as_view())
]