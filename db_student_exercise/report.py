import sqlite3
from items import Student, Cohort, Exercise, Instructor
class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )            

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from Student s
            join Cohort c on s.cohort_id = c.id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()
            print("\n***** ALL STUDENTS *****")
            [print(s) for s in all_students]

    def all_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda c, r: Cohort(
                r[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute('''
            SELECT
                c.id,
                c.name
            FROM Cohort c
            ''')

            all_cohorts = db_cursor.fetchall()
            print("\n***** ALL COHORTS *****")
            [print(c) for c in all_cohorts]

    def all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda c, r: Exercise(
                r[1], r[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.id,
                e.language,
                e.name
            FROM Exercise e
            """)

            all_exercises = db_cursor.fetchall()
            print("\n***** ALL EXERCISES *****")

            [print(e) for e in all_exercises]

    def all_instructors(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda c, r: Instructor(
                r[1], r[2], r[3], r[4], r[5]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                i.id,
                i.first_name,
                i.last_name,
                i.slack_handle,
                i.specialty,
                c.name
            FROM Instructor i
            LEFT JOIN Cohort c ON
                c.id = i.cohort_id
            """)

            all_instructors = db_cursor.fetchall()
            
            print("\n***** ALL INSTRUCTORS *****")
            [print(i) for i in all_instructors]

    def exercise(self, language = None):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda c, r: Exercise(
                r[1], r[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute(f"""
            SELECT
                e.id,
                e.language,
                e.name
            FROM Exercise e
            WHERE
                e.language = "{language}"
            """)

            exercises = db_cursor.fetchall()
            print(f"\n***** {language.upper() if language else 'ALL' } EXERCISES *****")
            [print(e) for e in exercises]

    def exercises_with_students(self):
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.id 'Excercise Id',
                e.name 'Exercise',
                s.id 'Student Id',
                s.first_name 'First Name',
                s.last_name 'Last Name'
            FROM Exercise e
            JOIN Student_Exercise se ON se.excercise_id = e.id
            JOIN Student s ON s.id = se.student_id
            """)

            dataset = db_cursor.fetchall()

            for r in dataset:
                e_id = r[0]
                e_name = r[1]
                s_id = r[2]
                s_name = f"{r[3]} {r[4]}"

                if e_name not in exercises:
                    exercises[e_name] = [s_name]
                else:
                    exercises[e_name].append(s_name)
                    
            print("\n***** ALL EXERCISES WITH STUDENTS *****")
            for e_name, students in exercises.items():
                print(e_name)
                for student in students:
                    print(f"\t* {student}")

    def student_with_exercises(self):
        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.id 'Excercise Id',
                e.name 'Exercise',
                s.id 'Student Id',
                s.first_name 'First Name',
                s.last_name 'Last Name'
            FROM Exercise e
            JOIN Student_Exercise se ON se.excercise_id = e.id
            JOIN Student s ON s.id = se.student_id
            """)

            dataset = db_cursor.fetchall()

            for r in dataset:
                e_id = r[0]
                e_name = r[1]
                s_id = r[2]
                s_name = f"{r[3]} {r[4]}"

                if s_name not in students:
                    students[s_name] = [e_name]
                else:
                    students[s_name].append(e_name)
                    
            print("\n***** ALL STUDENTS WITH EXERCISES *****")
            for student, exercises in students.items():
                print(f"\n{student} is working on:")
                for exercise in exercises:
                    print(f"\t* {exercise}")
                
    def assigned_exercises(self):
        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT
                i.first_name,
                i.last_name,
                e.name
            FROM Student_Exercise se
            JOIN Instructor i ON i.id = se.instructor_id
            JOIN Exercise e ON e.id = se.excercise_id
            """)

            instructor_assigned = db_cursor.fetchall()
            
            for first, last, exercise in instructor_assigned:
                if f"{first} {last}" not in instructors:
                    instructors[f"{first} {last}"] = [exercise]
                else:
                    if exercise not in instructors[f"{first} {last}"]:
                        instructors[f"{first} {last}"].append(exercise)

            print("\n***** ASSIGNED EXERCISES *****")
            for instructor, exercises in instructors.items():
                print(f"\n{instructor} has assigned:")
                for exercise in exercises:
                    print(f"\t* {exercise}")
    
    def popular_exercises(self):
        exercises = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                s.first_name,
                s.last_name,
                e.name
            FROM Student_Exercise se
            JOIN Student s ON
                s.id = se.student_id
            JOIN Exercise e ON
                e.id = se.excercise_id
            """)

            data = db_cursor.fetchall()
            print("\n***** POPULAR EXERCISES *****")
            for first, last, ex_name in data:
                if ex_name not in exercises:
                    exercises[ex_name] = [f"{first} {last}"]
                elif f"{first} {last}" not in exercises[ex_name]:
                    exercises[ex_name].append(f"{first} {last}")

            for name, students in exercises.items():
                print(f"\n{name} is being worked on by:")
                for student in students:
                    print(f"\t* {student}")