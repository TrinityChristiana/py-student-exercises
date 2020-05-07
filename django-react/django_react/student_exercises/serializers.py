from rest_framework import serializers
from .models import Cohort, Exercise, Instructor, Student, StudentExercise


class CohortSerializer(serializers.ModelSerializer):
    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # instructors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cohort
        fields = ('id', 'name')


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'language')


class InstructorSerializer(serializers.ModelSerializer):
    # cohort = CohortSerializer(read_only=True)

    class Meta:
        model = Instructor
        fields = ('id', 'first_name', 'last_name',
                  'cohort', 'slack_handle', 'specialty')


class StudentSerializer(serializers.ModelSerializer):
    # cohort = CohortSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'cohort', 'slack_handle')


class StudentSerializer(serializers.ModelSerializer):
    # cohort = CohortSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'cohort', 'slack_handle')


class StudentExerciseSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(read_only=True)
    # exercise = ExerciseSerializer(read_only=True)
    # instructor = InstructorSerializer(read_only=True)

    class Meta:
        model = StudentExercise
        fields = ('id', 'student', 'exercise', 'instructor')
