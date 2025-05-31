CREATE DATABASE IF NOT EXISTS SimpleStore;
USE SimpleStore;

CREATE TABLE Sales (
	SalesID INT AUTO_INCREMENT PRIMARY KEY,
    Product VARCHAR(50),
    Category VARCHAR(50),
    Amount DECIMAL(10,2),
    SaleDate DATE
);

DROP TABLE Sales;
SELECT * FROM Sales;
TRUNCATE TABLE Sales;

INSERT INTO Sales (Product, Category, Amount, SaleDate) 
VALUES
('Layers', 'Stationery', 25, '2024-03-01'),
('Notebook', 'Stationery', 50, '2024-03-01'),
('Mouse', 'Electronics', 500, '2024-03-02'),
('Keyboard', 'Electronics', 700, '2024-03-02'),
('Charger', 'Electronics', 300, '2024-03-03'),
('Bag', 'Accessories', 1000, '2024-03-04'),
('CoolingFan', 'Accessories', 700, '2024-03-05');


-- SUBQUERY
SELECT Product, Amount
FROM Sales
WHERE Amount > (SELECT AVG(Amount) FROM Sales);

SELECT Category, SUM(Amount)
FROM Sales
GROUP BY Category
HAVING SUM(Amount) > 1000;

-- CTE: Common Table Expression
WITH CategoryTotals AS (
	SELECT Category, SUM(Amount) AS TotalSales
    FROM Sales
    GROUP BY Category
)
SELECT Category, TotalSales
FROM CategoryTotals
WHERE TotalSales > 500;

WITH CategoryTotals AS (
    SELECT Category, SUM(Amount) AS TotalSales
    FROM Sales
    GROUP BY Category
),
FilteredSales AS (
    SELECT s.Product, s.Category, s.Amount
    FROM Sales s
    INNER JOIN CategoryTotals ct ON s.Category = ct.Category
    WHERE ct.TotalSales > 1000
)
SELECT DISTINCT Product, Category, Amount
FROM FilteredSales;


-- VIEW Virtual Table
CREATE VIEW CategorySales AS
SELECT Category, SUM(Amount) AS TotalSales
FROM Sales
GROUP BY Category;

SELECT * FROM CategorySales WHERE TotalSales > 500;














