from report import StudentExerciseReports

report = StudentExerciseReports()
# Display all cohorts.
report.all_cohorts()

# Display all exercises.
report.all_exercises()

# Display all JavaScript exercises.
report.exercise(language="JavaScript")

# Display all Python exercises.
report.exercise(language="Python")

# Display all C# exercises.
report.exercise(language="C#")

# Display all students with cohort name.
report.all_students()

# Display all instructors with cohort name.
report.all_instructors()

report.exercises_with_students()

# Practice: Student Workload
report.student_with_exercises()

# Practice: Assigned Exercises
report.assigned_exercises()

# Practice: Popular Exercises
report.popular_exercises()

