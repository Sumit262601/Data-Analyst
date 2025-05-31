CREATE DATABASE IF NOT EXISTS StudentDB;
USE StudentDB;
DROP DATABASE studentdb;

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Class VARCHAR(10)
);

-- Create a Subject Table
CREATE TABLE Subjects (
    SubjectID INT PRIMARY KEY,
    StudentID INT,
    SubjectName VARCHAR(100),
    Marks INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Insert data into Students
INSERT INTO Students (StudentID, Name, Age, Class) VALUES
(1, 'Alice Johnson', 14, '8A'),
(2, 'Brian Smith', 15, '9B'),
(3, 'Catherine Lee', 16, '10A'),
(4, 'David Brown', 14, '8B'),
(5, 'Eva Green', 17, '11A'),
(6, 'Frank Miller', 15, '9A'),
(7, 'Grace Kim', 13, '7A'),
(8, 'Harry White', 16, '10B');

-- Insert data into Subjects
INSERT INTO Subjects (SubjectID, StudentID, SubjectName, Marks) 
VALUES
(1, 1, 'Math', 85),
(2, 1, 'Science', 90),
(3, 2, 'Math', 78),
(4, 2, 'English', 88),
(5, 3, 'Math', 92),
(6, 3, 'Science', 95),
(7, 4, 'Math', 70),
(8, 4, 'Science', 75),
(9, 5, 'Math', 88),
(10, 5, 'English', 82),
(11, 6, 'Math', 68),
(12, 6, 'Science', 74),
(13, 7, 'English', 80);


SELECT * FROM Students;
SELECT * FROM Subjects;
TRUNCATE TABLE Students;

SELECT * FROM Students WHERE Age > 15;

UPDATE Students SET Class = '10C' WHERE StudentID = 3;

DELETE FROM Students WHERE StudentID = 4;

SELECT Class, COUNT(*) AS TotalClass FROM Students GROUP BY Class;

SELECT s.Name, s.Class, sub.SubjectName, sub.Marks
FROM Students s
LEFT JOIN Subjects sub ON s.StudentID = sub.SubjectID;

UNION

SELECT s.Name, sub.SubjectName, sub.Marks
FROM Students s
RIGHT JOIN Subjects sub ON s.StudentID = sub.SubjectID;

SELECT DISTINCT s.Name, s.StudentID
FROM Students s
JOIN Subjects sub ON s.StudentID = sub.StudentID
WHERE sub.Marks > 80;

SELECT DISTINCT s.Name, sub.SubjectName
FROM students s
LEFT JOIN subjects sub ON s.StudentID = sub.StudentID
WHERE sub.Marks > 80;