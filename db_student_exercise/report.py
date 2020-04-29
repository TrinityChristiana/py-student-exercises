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

    def all_student_exercises(self):
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
                    
            print("\n***** ALL STUDENT EXERCISES *****")
            for e_name, students in exercises.items():
                print(e_name)
                for student in students:
                    print(f"\t* {student}")
