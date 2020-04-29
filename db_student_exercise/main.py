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

report.all_student_exercises()