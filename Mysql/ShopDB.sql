CREATE DATABASE IF NOT EXISTS ShopDB;
USE ShopDB;

SELECT DATABASE();

CREATE TABLE Customers(
	CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Address VARCHAR(200)
);

INSERT INTO Customers(Name, Email, Address)
VALUES
("Sumit", "sumit@gmail.com", "Delhi"),
("Sweety", "sweety@gmail.com", "Mumbai"),
("Atul", "atul@gmail.com", "Delhi"),
("Amrita", "amrita@gmail.com", "Jaipur"),
("Anjali", "anjali@gmail.com", "Delhi"),
("Sahil", "sahil@gmail.com", "Bengalore"),
("Rinnki Ponding", "rinnkiponding@gmail.com", "Kerala"),
("Mili", "mili@gmail.com", "Odisha")
;

SELECT * FROM Customers;
TRUNCATE Customers;
ALTER TABLE Customers RENAME COLUMN Address TO City;
SELECT Name, Email FROM Customers;

-- DISTINCT DO NOT CALL REPEATED DATA
SELECT DISTINCT City FROM Customers;

-- FILTRING
SELECT * FROM Customers WHERE City LIKE '%Pune%';
SELECT * FROM Customers WHERE Name="Amrita" AND City LIKE "%Jaipur%";
SELECT * FROM Customers WHERE City NOT LIKE '%Delhi%';

-- FILTRING BY ORDER (ASC/DESC)
SELECT * FROM Customers ORDER BY City ASC;

-- UPDATE FUNCTION
UPDATE Customers SET City='Pune' WHERE CustomerID=1;

-- DELETE FUNCTION
DELETE FROM Customers
WHERE City = 'Delhi';

DELETE FROM Customers
WHERE Name="Mili";



/* 					 Aggregation And Grouping Data  			*/
/*

				--	Aggregation  --
						-> COUNT()
						-> SUM()
						-> MIN()
						-> MAX()
						-> AVG()


				--  Filtering Group  --
						HAVING
						WHERE
                        
                        
				--  Grouping Data  --
						GROUP BY
*/


CREATE TABLE Products (
    Product VARCHAR(50),
    Category VARCHAR(50),
    Amount DECIMAL(10,2),
    SaleDate DATE
);
DROP TABLE Products;

INSERT INTO Products (Product, Category, Amount, SaleDate) 
VALUES
('Layers', 'Stationery', 25, '2024-03-01'),
('Notebook', 'Stationery', 50, '2024-03-01'),
('Mouse', 'Electronics', 500, '2024-03-02'),
('Keyboard', 'Electronics', 700, '2024-03-02'),
('Charger', 'Electronics', 300, '2024-03-03'),
('Bag', 'Accessories', 1000, '2024-03-04');

TRUNCATE TABLE Products;
SELECT * FROM Products;

-- COUNT()
SELECT COUNT(Amount) FROM Products;

-- SUM()
SELECT SUM(Amount) FROM Products;

-- AVG()
SELECT AVG(Amount) FROM Products;

-- MIN()
SELECT MIN(Amount) FROM Products;

-- MAX()
SELECT MAX(Amount) FROM Products;

-- GROUP BY / HAVING
SELECT Category, SUM(Amount)
FROM Products
GROUP BY Category
HAVING SUM(Amount) > 1000;


































