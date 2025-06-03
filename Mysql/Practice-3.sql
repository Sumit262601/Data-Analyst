CREATE DATABASE practice2;
USE practice2;

-- COR CUSTOMER TABLE 
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(100),
    City VARCHAR(50)
);
INSERT INTO Customers VALUES
(1, 'Alice Johnson', 'alice@example.com', 'New York'),
(2, 'Bob Smith', 'bob@example.com', 'Los Angeles'),
(3, 'Charlie Lee', 'charlie@example.com', 'Chicago'),
(4, 'Diana Rose', 'diana@example.com', 'Houston'),
(5, 'Ethan Brown', 'ethan@example.com', 'Phoenix');


-- FOR PRODUCTS TABLE
CREATE TABLE Products (
	ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Catrgory VARCHAR(50),
    price DECIMAL(10, 2)
);
INSERT INTO Products VALUES
(1, 'Laptop', 'Electronics', 900.00),
(2, 'Smartphone', 'Electronics', 500.00),
(3, 'Desk Chair', 'Furniture', 120.00),
(4, 'Notebook', 'Stationery', 5.00),
(5, 'Pen Set', 'Stationery', 10.00);


-- FOR ORDERS TABLE
CREATE TABLE Orders (
	OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
INSERT INTO Orders VALUES
(101, 1, 1, '2024-01-15', 1),
(102, 2, 2, '2024-02-10', 2),
(103, 1, 5, '2024-03-05', 5),
(104, 3, 3, '2024-03-20', 1),
(105, 4, 4, '2024-04-12', 10),
(106, 5, 1, '2024-05-01', 1),
(107, 3, 2, '2024-05-15', 1);

select * from orders;
select * from products;
select * from customers;
select Name, City from customers;

-- Fetch all records from the Orders table where the Amount is greater than 200.
SELECT o.OrderDate, (o.Quantity * p.Price ) AS Amount
FROM Orders o
LEFT JOIN Products p ON o.ProductID = p.ProductID
WHERE (o.Quantity * p.Price) > 200;

-- Count the total number of customers in the Customers table.
SELECT COUNT(CustomerID) FROM customers;

SELECT SUM(p.Price * o.Quantity)  AS Amount
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID;

-- For each customer, display the maximum, minimum, and average order amount.
SELECT MIN(p.Price * o.Quantity)  AS Amount
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID;

SELECT MAX(p.Price * o.Quantity)  AS Amount
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID;

SELECT AVG(p.Price * o.Quantity)  AS Amount
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID;

-- List all orders sorted by Amount in descending order.
SELECT o.OrderID, (p.Price * o.Quantity) AS Amount
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID
ORDER BY Amount ASC;










