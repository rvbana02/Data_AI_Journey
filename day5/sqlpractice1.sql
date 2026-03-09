show databases;
create database student;
use student;
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
);
INSERT INTO students VALUES (1, 'Raj', 80);
INSERT INTO students VALUES (2, 'Amit', 55);
INSERT INTO students VALUES (3, 'Sita', 90);
SELECT * FROM students;

SELECT * FROM students
WHERE marks > 70;

select (name) from students;

SELECT * FROM students
where name="raj";
