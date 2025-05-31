USE retailstore;
SHOW tables;

SELECT * FROM customers;
SELECT * FROM orders;


SELECT customers.CustomerName, orders.Product, orders.Amount
FROM customers
INNER JOIN orders ON customers.CustomerID = orders.CustomerID;

