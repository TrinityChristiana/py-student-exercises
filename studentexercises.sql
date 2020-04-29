-- Create Cohort TABLE
-- CREATE TABLE Cohort (
-- 	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
-- 	name TEXT NOT NULL UNIQUE
-- );


-- Create Student TABLE
-- CREATE TABLE Student (
-- 	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
-- 	first_name TEXT NOT NULL UNIQUE,
-- 	last_name TEXT NOT NULL UNIQUE,
-- 	slack_handle TEXT NOT NULL UNIQUE,
-- 	cohort_id INTEGER NOT NULL,
-- 	FOREIGN KEY (cohort_id) 
-- 		REFERENCES Cohort(id)
-- );


-- Create Instructor TABLE
-- CREATE TABLE Instructor (
-- 	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
-- 	first_name TEXT NOT NULL UNIQUE,
-- 	last_name TEXT NOT NULL UNIQUE,
-- 	slack_handle TEXT NOT NULL UNIQUE,
-- 	specialty TEXT NOT NULL,
-- 	cohort_id INTEGER NOT NULL,
-- 	FOREIGN KEY (cohort_id) 
-- 		REFERENCES Cohort(id)
-- );


-- Create Excercise TABLE
-- CREATE TABLE Exercise (
-- 	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
-- 	language TEXT NOT NULL,
-- 	name TEXT NOT NULL
-- );


-- Create Student_Exercise Table
-- CREATE TABLE Student_Exercise (
-- 	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
-- 	student_id Integer NOT NULL,
-- 	excercise_id Integer NOT NULL,
-- 	FOREIGN KEY (student_id) REFERENCES Student(id),
-- 	FOREIGN KEY (excercise_id) REFERENCES Exercise(id)
-- );

-- Use the INSERT INTO SQL statement to create...

-- 3 cohorts
-- Insert INTO Cohort
-- 	(name)
-- VALUES
-- 	("Cohort 38");
--
-- Insert INTO Cohort
-- 	(name)
-- VALUES
-- 	("Cohort 39");
-- 	
-- Insert INTO Cohort
-- 	(name)
-- VALUES
-- 	("Cohort 37");


-- 5 exercises
-- Insert INTO Exercise
-- 	(language, name)
-- Values
-- 	("Python", "Student Exercises"),
-- 	("HTML", "Celebrity Tribute"),
-- 	("Ruby", "Toy App"),
-- 	("JavaScript", "React Nutshell"),
-- 	("SQL", "Music History")

-- 3 instructors
-- Insert INTO Instructor
-- 	(first_name, last_name, slack_handle, specialty, cohort_id)
-- VALUES
-- 	("Jisie", "David", "jisie", "Teaching Back-End", 1),
-- 	("Kristen", "Norris", "kristen.norris", "Helping Students", 2),
-- 	("Bryan", "Nilsen", "Bryan Nilsen", "Leaving Us", 3)
-- 	

-- 7 students (don't put all students in the same cohort)
-- Insert INTO Student
-- 	(first_name, last_name, slack_handle, cohort_id)
-- VALUES
-- 	("Trinity", "Terry", "Trinity", 1),
-- 	("Roxanne", "Nasraty", "Roxanne", 2),
-- 	("Alyssa", "Nycum", "Alyssa Nycum", 3),
-- 	("Katie", "Wohl", "Katie Wohl", 1),
-- 	("Mollie", "Goforth", "Mollie", 2),
-- 	("Sofia", "Candiani", "Sofiancandiani", 3),
-- 	("Keaton", "Williamson", "keatonwilliamson", 3)
	

-- Assign 2 exercises to each student
-- Insert INTO Student_Exercise
-- 	(student_id, excercise_id)
-- VALUES
-- 	(1, 1),
-- 	(1, 2),
-- 	(2, 4),
-- 	(2, 3),
-- 	(3, 2),
-- 	(3, 1),
-- 	(4, 5),
-- 	(4, 4),
-- 	(5, 3),
-- 	(5, 2),
-- 	(6, 1),
-- 	(6, 5),
-- 	(7, 4),
-- 	(7, 3)
	

