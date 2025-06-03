CREATE DATABASE IF NOT EXISTS Customers;
USE Customers;

--  Create Data Table for Customers
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(50)
);

--  Create Data Table for Orders
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(10, 2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
SELECT * FROM Orders;
-- INSERT CUSTOMERS DATA
INSERT INTO Customers (name, email, city) VALUES
('Amit Sharma', 'amit.sharma@example.com', 'Delhi'),
('Sneha Verma', 'sneha.verma@example.com', 'Mumbai'),
('Rahul Mehta', 'rahul.mehta@example.com', 'Bangalore'),
('Priya Desai', 'priya.desai@example.com', 'Delhi'),
('Vikram Singh', 'vikram.singh@example.com', 'Hyderabad');

-- INSERT ORDERS DATA
INSERT INTO Orders (customer_id, amount, order_date) VALUES
(1, 2500.00, '2024-12-01'),
(2, 1300.50, '2024-12-03'),
(1, 4999.99, '2024-12-15'),
(3, 799.00,  '2024-12-18'),
(2, 1599.75, '2025-01-04'),
(5, 10000.00, '2025-01-05'),
(1, 349.99,  '2025-01-07'),
(4, 2000.00, '2025-01-10'),
(3, 1499.49, '2025-01-11'),
(1, 999.99,  '2025-01-15');

-- first
SELECT cu.customer_id, cu.name, COUNT(od.order_id) AS TotalOrders
FROM customers cu
LEFT JOIN orders od ON cu.customer_id = od.customer_id
GROUP BY cu.customer_id, cu.name
ORDER BY TotalOrders DESC;

SELECT cu.customer_id, cu.name, cu.email, cu.city
FROM Customers cu
LEFT JOIN Orders od ON cu.customer_id = od.customer_id
WHERE od.order_id IS NULL;

 select * from  Customers where city='Delhi';

SELECT cu.customer_id, cu.name, cu.city, SUM(od.Amount) AS TotalAmount
FROM customers cu
LEFT JOIN orders od ON cu.customer_id = od.customer_id
WHERE City="Hyderabad"
GROUP BY cu.customer_id, cu.name, cu.city
HAVING SUM(od.amount) > 10000;

select (
	select name from Customers
) as list;






