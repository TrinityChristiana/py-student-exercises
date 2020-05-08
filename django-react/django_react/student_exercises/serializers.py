from rest_framework import serializers
from .models import Cohort, Exercise, Instructor, Student, StudentExercise


class CohortSerializer(serializers.ModelSerializer):
    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # instructors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='cohort-detail')
    class Meta:
        model = Cohort
        fields = ('id',"url", 'name')
        depth = 1


class ExerciseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='exercise-detail')
    class Meta:
        model = Exercise
        fields = ('id',"url",'name', 'language')
        depth = 1


class InstructorSerializer(serializers.ModelSerializer):
    # cohort = CohortSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='instructor-detail')
    class Meta:
        model = Instructor
        fields = ('id',"url", 'first_name', 'last_name',
                  'cohort', 'slack_handle', 'specialty')
        depth = 1


class StudentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='student-detail')
    class Meta:
        model = Student
        fields = ("id", "first_name", "url", "last_name", "slack_handle", "cohort")
        depth = 1


        


class StudentExerciseSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(read_only=True)
    # exercise = ExerciseSerializer(read_only=True)
    # instructor = InstructorSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='student_exercise-detail')
    class Meta:
        model = StudentExercise
        fields = ('id',"url", 'student', 'exercise', 'instructor')
        depth = 1

class Error(object):
    def __init__(self, error):
        self.error = error
class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Error(**validated_data)




