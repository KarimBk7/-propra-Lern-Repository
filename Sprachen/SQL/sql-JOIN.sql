DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

-- A1 
CREATE TABLE students(
  name TEXT,
  age INT,
  id INT
);
 
CREATE TABLE courses(
   name TEXT,
   prof TEXT,
   id INT
);

INSERT INTO students
VALUES 	('Alice', 22, 1),
        ('Bob', 20, 2),
        ('Charlie', 25, 1),
        ('David', 23, 3),
        ('Emma', 21, 2),
        ('Frank', 24, 3),
        ('Grace', 22, 1),
        ('Hannah', 19, 2),
        ('Ian', 26, 1),
        ('Jessica', 20, 3);
      
INSERT INTO courses
VALUES 	('Mathematics', 'Dr. Smith', 1),
        ('Computer Science', 'Prof. Johnson', 2),
        ('Literature', 'Dr. Brown', 1),
        ('History', 'Prof. Davis', 2),
        ('Physics', 'Dr. Wilson', 1),
        ('Biology', 'Prof. Martinez', 2),
        ('Chemistry', 'Dr. Lee', 1),
        ('Art', 'Prof. Clark', 2),
        ('Music', 'Prof. Adams', 1),
        ('Physical Education', 'Coach Taylor', 2);
      
-- A2 
SELECT students.name, courses.name FROM students
INNER JOIN courses ON students.id = courses.id;

-- A3
SELECT students.name FROM students
INNER JOIN courses ON students.id = courses.id
WHERE courses.prof = 'Dr. Smith';

-- A4 
SELECT students.name, courses.name FROM courses
LEFT JOIN students ON students.id = courses.id;

-- A5 
SELECT c.prof, c.name, s.name FROM courses AS c 
LEFT JOIN students AS s 
	ON c.id = s.id;
   
-- A6 
SELECT c.name, s.name FROM courses AS c 
LEFT JOIN students AS s 
	ON c.id = s.id;
    
-- A7
SELECT c.name, s.name, c.id FROM courses AS c 
LEFT JOIN students AS s 
	ON c.id = s.id
WHERE c.id = 1;

-- A8 
SELECT s.name as Person FROM students AS s
LEFT JOIN courses ON courses.id = s.id
UNION
SELECT c.prof AS Person FROM courses AS c
LEFT JOIN students ON c.id = students.id;

-- A9 
SELECT s.id FROM students AS s 
LEFT JOIN courses as c ON c.id = s.id 
UNION 
SELECT c.id FROM courses AS c 
LEFT JOIN students AS s ON c.id = s.id;

-- A10 
SELECT s.name as Person FROM students AS s
LEFT JOIN courses ON courses.id = s.id
UNION ALL
SELECT c.prof AS Person FROM courses AS c
LEFT JOIN students ON c.id = students.id;

-- A11
SELECT age AS value
FROM students
UNION ALL
SELECT id
FROM courses;

-- A12 
SELECT s.name FROM students as s 
LEFT JOIN courses AS c 
